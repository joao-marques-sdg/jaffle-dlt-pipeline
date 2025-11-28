import dlt
from dlt.sources.helpers.rest_client import RESTClient


BASE_URL = "https://jaffle-shop.scalevector.ai/api/v1"


def paged_resource(endpoint: str):
    client = RESTClient(BASE_URL)

    @dlt.resource(name=endpoint, parallelized=True)
    def get_pages():
        page = 1
        while True:
            response = client.get(f"/{endpoint}?page={page}")
            data = response.json()
            if isinstance(data, dict):
                items = data.get("data",[])
            elif isinstance(data, list):
                items = data
            else:
                items=  []
            elif not items:
                break

            yield items  # yield whole page

            page += 1

    return get_pages()


@dlt.source
def jaffle_shop_source():
    yield paged_resource("customers")
    yield paged_resource("orders")
    yield paged_resource("products")


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="jaffle_shop_pipeline",
        destination="duckdb",
        dataset_name="jaffle_data",
    )

    load_info = pipeline.run(jaffle_shop_source())
    print(load_info)

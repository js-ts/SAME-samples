from typing import Dict
from typing import NamedTuple
import json

import kfp.dsl as dsl
import kfp
from kfp.components import func_to_container_op, InputPath, OutputPath
import kfp.compiler as compiler

import pprint


def python_function_factory(
    function_name: str,
    packages: list,
    base_image_name="python:3.9-slim-buster",
    ann: list = None,
):
    return func_to_container_op(
        func=function_name,
        base_image=base_image_name,
        packages_to_install=packages,
        annotations=ann,
    )


def download_data(url: str, output_text_path: OutputPath(str)):
    import requests

    req = requests.get(url)
    url_content = req.content

    with open(output_text_path, "wb") as writer:
        writer.write(url_content)


def train(
    train_data: InputPath(),
    test_data: InputPath(),
    total: InputPath(),
    metrics_path: OutputPath("Metrics"),
):
    import json

    print("Inside training")

    metrics = {
        "metrics": [
            {
                "name": "final_total",  # The name of the metric. Visualized as the column name in the runs table.
                "numberValue": total,  # The value of the metric. Must be a numeric value.
                "format": "RAW",  # The optional format of the metric. Supported values are "RAW" (displayed in raw format) and "PERCENTAGE" (displayed in percentage format).
            }
        ]
    }

    print("Total: %s" % total)
    with open(metrics_path, "w") as f:
        json.dump(metrics, f)


@dsl.pipeline(
    name="Simple Overrideable Data Connector",
    description="A simple component designed to demonstrate a multistep pipeline.",
)
def simple_pipeline_component(train_data="", test_data="", epochs=2, sha=""):
    training_dataframe = None
    testing_dataframe = None
    if train_data_url == "": 
    train_data_url = "https://same-project.github.io/samples//train.csv"
    test_data_url = "https://same-project.github.io/samples/houseprice/test.csv"
    train_download_op = download_data_factory(train_data_url)
    train_download_op.set_display_name("Download training data")
    test_download_op = download_data_factory(test_data_url)
    test_download_op.set_display_name("Download test data")

    add_op = func_to_container_op(func=add)
    multiply_op = func_to_container_op(func=multiply)
    subtract_op = func_to_container_op(func=substract)
    divide_op = func_to_container_op(func=divide)

    train_op = func_to_container_op(func=train)

    # input 42
    starting_input = 42

    # add 8 to 42 = 50
    add_task = add_op(starting_input, 8)

    # substract 18 from 42 = 24
    subtract_task = subtract_op(starting_input, 18)

    # multiply output 24 * 3 = 72
    multiply_task = multiply_op(subtract_task.output, 3)

    # add 50 + output of multiple = 122
    add_multiply_task = add_op(50, multiply_task.output)

    # execute parallel for items 8 paired items = 100
    paired_items = [
        {"a": 1, "b": 2},
        {"a": 3, "b": 4},
        {"a": 5, "b": 6},
        {"a": 7, "b": 8},
    ]

    all_results = []
    # Cannot implement the below until Kubeflow V2 that has a fan in operator (https://docs.google.com/document/d/1fHU29oScMEKPttDA1Th1ibImAKsFVVt2Ynr4ZME05i0/edit)
    # with dsl.ParallelFor(paired_items, parallelism=4) as item:
    #     parallel_multiply_task = multiply_op(item.a, item.b)
    #     all_results.append(parallel_multiply_task)

    # aggregate_task = add_op(0, 0)
    # for i in all_results:
    #     aggregate_task = add_op(aggregate_task.outputs["result"], i.outputs["result"])

    parallel_multiply_task_0 = multiply_op(0, 0)
    aggregate_task_0 = add_op(0, parallel_multiply_task_0.output)

    parallel_multiply_task_1 = multiply_op(paired_items[0]["a"], paired_items[0]["b"])
    aggregate_task_1 = add_op(aggregate_task_0.output, parallel_multiply_task_1.output)

    parallel_multiply_task_2 = multiply_op(paired_items[1]["a"], paired_items[1]["b"])
    aggregate_task_2 = add_op(aggregate_task_1.output, parallel_multiply_task_2.output)

    parallel_multiply_task_3 = multiply_op(paired_items[2]["a"], paired_items[2]["b"])
    aggregate_task_3 = add_op(aggregate_task_2.output, parallel_multiply_task_3.output)

    parallel_multiply_task_4 = multiply_op(paired_items[3]["a"], paired_items[3]["b"])
    aggregate_task_4 = add_op(aggregate_task_3.output, parallel_multiply_task_4.output)

    # add add_multiply to aggregate_task_4 = 222
    mid_total_task = add_op(add_multiply_task.output, aggregate_task_4.output)

    # Final mid_total_task + add_task = 272
    final_total_task = add_op(mid_total_task.output, add_task.output)

    print("Final Total: {final_total_task.output}")

    train_task = train_op(
        train_data="",
        test_data="",
        total=final_total_task.output,
    )

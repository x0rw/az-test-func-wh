import azure.functions as func
import datetime
import json
import logging
import urllib

webhook_url = (
    "https://hooks.slack.com/services/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"
)
app = func.FunctionApp()


@app.route(route="az_test", auth_level=func.AuthLevel.ANONYMOUS)
def az_test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        dataj = {"text": f"hello {name}"}
        req = urllib.request.Request(
            webhook_url, data=json.dumps(dataj).encode("utf-8")
        )
        response = urllib.request.urlopen(req)

        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully."
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )


from django.shortcuts import render
from django.conf import settings

import boto3
import json

brt = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")


def portfolio(request):

    # # Change here
    # recommendations_prompt = "what is taylor's university"

    # recommendations_input = "\n\nHuman: {}\n\nAssistant:".format(recommendations_prompt)

    # recommendations_body = json.dumps({
    # "prompt": recommendations_input,
    # "max_tokens_to_sample": 300,
    # "temperature": 0.1,
    # "top_p": 0.9,
    # })

    # modelId = 'anthropic.claude-v1'
    # accept = 'application/json'
    # contentType = 'application/json'

    # response = brt.invoke_model(body=recommendations_body, modelId=modelId, accept=accept, contentType=contentType)

    # response_body = json.loads(response.get('body').read())

    # portfolio_recommendations = response_body.get('completion')

    # # Change here
    # summary_prompt = "summary of the bee movie"

    # summary_input = "\n\nHuman: {}\n\nAssistant:".format(summary_prompt)

    # summary_body = json.dumps({
    # "prompt": summary_input,
    # "max_tokens_to_sample": 300,
    # "temperature": 0.1,
    # "top_p": 0.9,
    # })

    # response = brt.invoke_model(body=summary_body, modelId=modelId, accept=accept, contentType=contentType)

    # response_body = json.loads(response.get('body').read())

    # summary = response_body.get('completion')


    # context = {"recommendations" : portfolio_recommendations, "summary": summary}
    return render(request, "portfolio/portfolio.html", settings.PORTFOLIO)
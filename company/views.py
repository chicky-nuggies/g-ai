from django.shortcuts import render
from django.http import HttpResponse
import requests

import boto3
import json

brt = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")


def company(request):

        if request.method == 'POST':
            user_input = request.POST['user_input']

            # Clean and format user input
            clean_input = user_input.strip().lower()

            final_input = "\n\nHuman: {}\n\nAssistant:".format(clean_input)
            print(clean_input)


            body = json.dumps({
            "prompt": final_input,
            "max_tokens_to_sample": 300,
            "temperature": 0.1,
            "top_p": 0.9,
            })

            modelId = 'anthropic.claude-v1'
            accept = 'application/json'
            contentType = 'application/json'

            response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

            response_body = json.loads(response.get('body').read())

            # text
            response = response_body.get('completion')

            # Prepare generated text for HTML display
            # escaped_text = cgi.escape(response)

            # Render HTML page with generated text
            context = {'generated_text': response}
            return render(request, "company/company.html", context)
        else:
            return render(request, "company/company.html")



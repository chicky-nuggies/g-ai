import boto3
from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd

data = pd.DataFrame({
    'feature1': pd.Series([1, 0, 0, 1]),
    'feature2': pd.Series([0, 1, 1, 0]),
    'target': pd.Series([1, 0, 1, 1])
})



def index(request):
    return render(request, "dashboard/index.html")


def predict_using_sagemaker_local_mode(request):
    # Create a SageMaker Estimator object.
    estimator = boto3.estimator.Estimator(
        role='arn:aws:iam::720170540593:role/TestSagemaker',
        image_name='sagemaker/tensorflow-mnist:latest',
        train_instance_count=1,
        train_instance_type='ml.m4.xlarge',
        model_name='my-model'
    )

    # Train the model.
    estimator.fit({
        data.to_csv()
        # 's3_data': '<YOUR_S3_DATA_URI>'
    })

    # Create a SageMaker Endpoint object.
    endpoint = boto3.endpoint.Endpoint(
        role='arn:aws:iam::720170540593:role/TestSagemaker',
        name='TestSagemakerEndpoint',
        model_name='my-model',
    )

    # Deploy the model.
    endpoint.deploy({
        'initial_instance_count': 1,
        'instance_type': 'ml.m4.xlarge',
    })

    # Send a prediction request to the endpoint.
    response = endpoint.invoke({
        'Body': [1200, 3, 2]
    })

    # Process the prediction response.
    prediction_output = response['Body']['Outputs'][0]['predict']
    confidence_score = response['Body']['Outputs'][0]['score']

    # Render the processed prediction data.
    context = {
        'prediction': prediction_output,
        'confidence': confidence_score
    }

    return render(request, 'prediction_template.html', context)



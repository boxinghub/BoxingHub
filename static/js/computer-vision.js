$('#imageUpload').change(function() {
    var reader = new FileReader();
    reader.onload = function(e) {
        $('#uploadedImage').attr('src', e.target.result);
        $('#uploadedImage').show();
    }
    reader.readAsDataURL(this.files[0]);
});

$('#runInference').click(function() {
    var formData = new FormData();
    formData.append('image', $('#imageUpload')[0].files[0]);

    $.ajax({
        url: '',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function(response) {
            var img_str = 'data:image/jpeg;base64,' + response.classified_image;
            $('#classifiedImage').attr('src', img_str);
            $('#classifiedImage').show();

            // Display the inference completion message
            let prediction = response.prediction;
            let confidence = response.confidence * 100;
            const formattedConfidence = confidence + '%';

            // console.log('Prediction: ' + prediction, 'Confidence: ' + formattedConfidence);

            const inference_result_message = `Inference completed. The image is classified as <strong style="color: red;">${prediction}</strong> with a confidence of <strong style="color: red;">${formattedConfidence}</strong>.<br>`;
            const chatbot_message = `Please try our <strong style="color: red;">boxing chatbot</strong> at the <strong>bottom right</strong>.`;

            // add these two messages to the messageAfterInference p tag
            $('#messageAfterInference').html(inference_result_message + chatbot_message);
            $('#messageAfterInference').show();;
        },
        error: function(response) {
            alert('Error running inference');
        }
    });
});
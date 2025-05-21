import os
from django.shortcuts import render
from django.conf import settings
from .forms import AudioUploadForm
from .speech_transcription_diarization import speech_to_text_with_speaker_diarization
from main.utils import get_likes_and_loves


def transcribe_and_diarize(request):
    transcript = None
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = form.cleaned_data['audio_file']
            audio_path = os.path.join(settings.AUDIO_ROOT, audio_file.name)

            # Save the uploaded audio file
            with open(audio_path, 'wb+') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            # Run the speech-to-text and speaker diarization
            transcript = speech_to_text_with_speaker_diarization(audio_path)

    else:
        form = AudioUploadForm()

    likes, loves = get_likes_and_loves()
    context = {
        'likes': likes,
        'loves': loves,
        'active': 'ai-boxing',
        'form': form,
        'transcript': transcript
    }

    return render(request, 'nlp_app/nlp_app.html', context)

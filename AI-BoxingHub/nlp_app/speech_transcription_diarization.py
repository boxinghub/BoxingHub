'''
This is an AI program focusing on NLP: Speech-to-text and speaker diarization
'''
# Quick command to run the program: python nlp_app/speech_transcription_diarization.py

import time
import os
import pytz
import whisper
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pyannote.audio import Pipeline
from pydub import AudioSegment


def speaker_diarization(audio_file,
                        window_duration=1.0,
                        step_duration=0.5):
    """
    This function performs speaker diarization using a sliding window approach.
    Accept mp3 and wav audio formats.

    Args:
        audio_file (str): a string or Path instance pointing to the audio file
        window_duration (float): the duration of the sliding window in seconds
        step_duration (float): the duration of the step in seconds

    Returns:
        speaker_segments (dic): a dictionary containing speaker segments with timestamps
    """
    print("Speaker diarization started")
    load_dotenv()
    HUGGINGFACE_HUB_TOKEN = os.getenv("HUGGINGFACE_HUB_TOKEN")
    
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=HUGGINGFACE_HUB_TOKEN
    )

    # apply pretrained pipeline on your audio file
    diarization = pipeline(audio_file)
    
    speaker_segments = []
    # Extract speaker segments with timestamps
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        # time.time() returns timestamp is in Coordinated Universal Time (UTC)
        current_time = time.time()
        date = time.strftime("%Y-%m-%d")

        start_timestamp = current_time + turn.start
        end_timestamp = current_time + turn.end

        start_datetime = datetime.fromtimestamp(start_timestamp, tz=pytz.utc)
        end_datetime = datetime.fromtimestamp(end_timestamp, tz=pytz.utc)

        # Get timezone is in 'Asia/Dubai', which is Gulf Standard Time (GST), UTC+4
        dubai_tz = pytz.timezone('Asia/Dubai')

        # Convert the UTC datetimes to Dubai time
        adjust_start_time = start_datetime.astimezone(dubai_tz)
        adjust_end_time = end_datetime.astimezone(dubai_tz)

        formatted_start = adjust_start_time.strftime("%H:%M:%S")
        formatted_end = adjust_end_time.strftime("%H:%M:%S")
        
        start_seconds = float(str(turn.start)[:4])
        end_seconds = float(str(turn.end)[:4])

        speaker_dict = {speaker: {
            "date": date,
            "start_timestamp": formatted_start,
            "end_timestamp": formatted_end,
            "start_seconds": start_seconds,
            "end_seconds": end_seconds
        }}
        speaker_segments.append(speaker_dict)
    
    '''
    exmaple of speaker_segments:
    [{"SPEAKER_00": {
        "date": "2024-03-28",
        "start_timestamp": "16:46:22",
        "end_timestamp": "16:46:26",
        "start_seconds": "0.78",
        "end_seconds": "4.88"
        }
    }]
    '''
    return speaker_segments


def extract_audio_segment(input_file, start_time, end_time, output_file):
    """
    This function extracts a segment from an audio file and saves it as a new wav file.

    args:
        input_file (str): the path to the input audio file
        start_time (float): the start time in seconds
        end_time (float): the end time in seconds
        output_file (str): the path to the output audio file

    returns:
        None 
    """
    # Load the audio file
    audio_file = AudioSegment.from_file(input_file)

    # Define start and end time in seconds (multiply by 1000 for milliseconds)
    start_time = start_time * 1000
    end_time = end_time * 1000

    # Extract the segment
    extracted_segment = audio_file[start_time:end_time]

    # Save the segment as a new wav file
    extracted_segment.export(output_file, format="wav")


def transcribe_audio(audio_file):
    """
    This function transcribes the audio file with speaker-specific segments.

    args:
        audio_file (str): the path to the audio file
    
    returns:
        transcript (str): the transcribed text
    """
    model = whisper.load_model("base.en")
    transcript = model.transcribe(audio_file)
    return transcript["text"].strip()


def output_transcript(speaker_segments,
                      audio_file="static/audio/test_speech_diarization.wav",
                      output_file="static/text/dialogue.csv"):
    """
    This function writes the speaker-specific segments to a CSV file.

    args:
        speaker_segments (dict): the speaker-specific segments
        output_file (str): the path to the output file

    returns:
        None
    """
    # a list to store the speaker-specific segments
    dialogue = []

    with open(output_file, "a") as dialogue_record:
        # Extract the speaker-specific segments
        print("Extracting audio segment")
        for speaker_segment in speaker_segments:
            for speaker, segment in speaker_segment.items():
                start_seconds = segment["start_seconds"]
                end_seconds = segment["end_seconds"]

                output_audio = f"static/audio/{speaker}.wav" # extracted segments
                extract_audio_segment(audio_file, start_seconds, end_seconds, output_audio)
                transcript = transcribe_audio(output_audio)

                # Write the speaker, date, start time, end time, and transcript to a CSV file
                date = segment["date"]
                start_timestamp = segment["start_timestamp"]
                end_timestamp = segment["end_timestamp"]
                dialogue_dict = {'speaker': speaker,
                                'date': date,
                                'start_timestamp': start_timestamp,
                                'end_timestamp': end_timestamp,
                                'transcript': transcript
                                }
                dialogue.append(dialogue_dict)
                dialogue_text = f'{speaker},{date},{start_timestamp},{end_timestamp},"{transcript}"'
                dialogue_record.write("\n" + dialogue_text)
            
        print("Save speaker-specific segments to a CSV file")
        return dialogue


def speech_to_text_with_speaker_diarization(audio_file="static/audio/test_speech_diarization.wav"):
    """
    This function performs speech-to-text with speaker diarization.

    args:
        audio_file (str): the path to the audio file

    returns:
        None
    """
    speaker_segments = speaker_diarization(audio_file)
    dialogue = output_transcript(speaker_segments, audio_file)
    return dialogue


if __name__ == "__main__":
    # Start recording
    try:
        print("Speech-to-text and speaker diarization started")
        print("-" * 20)
        dialogue = speech_to_text_with_speaker_diarization()
        for record in dialogue:
            print(record)
    except KeyboardInterrupt:
        print("\nSpeech-to-text and speaker diarization stopped")
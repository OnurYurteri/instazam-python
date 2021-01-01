import os
import ffmpeg
import constants


def get_audio(file_in, file_name_out):
    stream = ffmpeg.input(file_in)
    audio = stream.audio

    output = os.path.join(constants.convert_dir,
                          file_name_out) + constants.audio_extension
    stream = ffmpeg.output(audio, output)
    ffmpeg.run(stream)
    print(output)

    return output

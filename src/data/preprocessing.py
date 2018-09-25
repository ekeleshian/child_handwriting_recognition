from PyPDF2 import PdfFileReader
import os

ROOT_TO_HANDWRITING_5 = '~/child_handwriting_recognition/data/handwriting_grade_5/'
ROOT_TO_TRANSCRIPTS_9 = '~/child_handwriting_recognition/data/transcripts_grade_9/'


def transcript_id_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(0)
        text = page.extractText()
        transcript_id = text[:8]
        return transcript_id


def rename_handwriting_files(root):
    upper_limit = len([name for name in os.listdir(root)])
    for i in range(2,upper_limit+2): # +2 b/c we are not starting from 1, and range function excludes upper bound
        path_to_file = f'{root}page-{i}.pdf'
        trans_id = transcript_id_extractor(path_to_file)
        os.rename(path_to_file, f'{root}{trans_id}_{i}.pdf')
    print('Success')


def rename_transcript_files(root):
    upper_limit = len([name for name in os.listdir(root)])
    for i in range(1,upper_limit+1): # +1 b/c range function excludes upper bound
        path_to_file = f'{root}page-{i}.pdf'
        trans_id = transcript_id_extractor(path_to_file)
        os.rename(path_to_file, f'{root}{trans_id}_{i}.pdf')
    print('Success')

rename_handwriting_files(ROOT_TO_HANDWRITING_5)

rename_transcript_files(ROOT_TO_TRANSCRIPTS_9)
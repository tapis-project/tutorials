import argparse, csv
from transformers import pipeline
import os.path
import os

parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--text', required=True)

# Parse the argument
args = str(parser.parse_args())
os.environ['SENTENCE_TRANSFORMERS_HOME'] = './.cache'
print("after os.env")
sentiment_analyzer = pipeline("sentiment-analysis")
result = sentiment_analyzer(args)


# Print output to screen and write to file
tapis_app_id = os.environ.get('_tapisAppId')
if tapis_app_id is None:
    # Not running under Tapis, write to /tmp
    print('Not running under Tapis. Writing output to /tmp\n')
    outputPath = '/tmp/output.txt'
else:
    # Running under Tapis.
    print('Running under Tapis: _tapisAppId=%s\n' % tapis_app_id)
    # If Docker, write to /TapisOutput,
    # else write to $_tapisExecSystemOutputDir
    tapis_sing_name = os.environ.get('SINGULARITY_NAME')
    if tapis_sing_name is None:
        print('Running via Tapis using Docker\n')
        outputPath = '/TapisOutput/output.txt'
    else:
        print('Running via Tapis using Singularity\n')
        outputDir = os.environ.get('_tapisExecSystemOutputDir')
        if outputDir is None:
            print('WARNING: _tapisExecSystemOutputDir not set. Using /tmp for output.')
            outputPath = '/tmp/output.txt'
        else:
            outputPath = outputDir + "/output.txt"
print('Using output path: %s\n' % outputPath)
f = open(outputPath, "a")
print(str(result))
f.write(str(result))
f.close()
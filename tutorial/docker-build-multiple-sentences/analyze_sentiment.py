import argparse, csv, os

from typing import List, Tuple
from typing_extensions import TypedDict

from transformers import pipeline

class Analysis(TypedDict):
    label: str
    score: float

AnalysisResult = List[Tuple[str, Analysis]]

def analyze(flags) -> AnalysisResult:
    """
    Function that analyzes the sentence that the user provided.

    Args:
        flags.sentence (str): The sentence to be analyzed.  
        flags.return_all_scores (str): Option to return all scores or just the highest.
        flags.model (str): A custom model from the Hugging Face hub.
            - optional model: j-hartmann/emotion-english-distilroberta-base

    Returns:
        results (List): sentiment analysis results.
    """
    # if the model is empty, it uses a basic model, else uses provided model
    model = flags.model if flags.model else None
    try:
        analyzer = pipeline("sentiment-analysis", model=model, return_all_scores=True)
    except Exception as e:
        raise Exception(f"Pipeline instantiation error: {e}")
    
    sentences = flags.sentences if flags.sentences != None else []
    
    files = flags.files if flags.files != None else []
    
    if len(files) == 0 and len(sentences) == 0:
        raise Exception("Must provide at least 1 sentence with --sentences flag or at least 1 file with the --files.")
    
    for path in files:
        if not os.path.isfile(path):
            raise Exception(f"A path provided in the --files flag is not a file | {path}")
        
        with open(path, mode="r") as file:
            sentences.append(file.read())
            
    analyses = analyzer(sentences)

    results = []
    for i, analysis in enumerate(analyses):
        results.append((sentences[i], analysis))
    print(results)
    return results

def store_results(results: AnalysisResult) -> None:
    """
    Function that stores the results into a csv file.

    Args:
        results (List): The results of the analysis.
    """
    # Determine where to write the output
    tapis_app_id = os.environ.get('_tapisAppId')
    if tapis_app_id is None:
        # Not running under Tapis, write to /tmp
        print('Not running under Tapis. Writing output to /tmp\n')
        outputPath = '/tmp/results.csv'
    else:
        # Running under Tapis.
        print('Running under Tapis: _tapisAppId=%s\n' % tapis_app_id)
        # If Docker, write to /TapisOutput,
        # else write to $_tapisExecSystemOutputDir
        tapis_sing_name = os.environ.get('SINGULARITY_NAME')
        if tapis_sing_name is None:
            print('Running via Tapis using Docker\n')
            outputPath = '/TapisOutput/results.csv'
        else:
            print('Running via Tapis using Singularity\n')
            outputDir = os.environ.get('_tapisExecSystemOutputDir')
            if outputDir is None:
                print('WARNING: _tapisExecSystemOutputDir not set. Using /tmp for output.')
                outputPath = '/tmp/results.csv'
            else:
                outputPath = outputDir + "/results.csv"
    print('Using output path: %s\n' % outputPath)

    # Print output to screen and write to file
    with open(outputPath, mode='a', newline='') as file:
        writer = csv.writer(file)
        labels = [label_data['label'] for _, analysis in results for label_data in analysis]
        labels.insert(0,"SENTENCE")
        writer.writerow(labels)
        for sentence, analysis in results:
            scores = ['%.3f' % label_data['score'] for label_data in analysis]
            writer.writerow([sentence] + scores)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sentences', type=str, nargs="+", help='Sentence for analyzing.')
    parser.add_argument('--files', type=str, nargs="+", help='File(s) upon which to run sentiment analysis')
    parser.add_argument('--model', default='j-hartmann/emotion-english-distilroberta-base', type=str, nargs='?', help='choose from the following models',
                        required=False,
                        choices=['j-hartmann/emotion-english-distilroberta-base','checkpoint','distilbert/distilbert-base-uncased-finetuned-sst-2-english']
                        )
    flags, _ = parser.parse_known_args()

    store_results(analyze(flags))

if __name__ == '__main__':
    main()

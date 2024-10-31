from tqdm import tqdm

def generate_dataset(sentences, progress_updates=None):
    dataset = []
    for i, sentence in tqdm(enumerate(sentences), desc="Generating Dataset", total=len(sentences)):
        dataset.append({"id": i, "text": sentence})
        if progress_updates is not None:
            progress_updates.append(i)
    return dataset

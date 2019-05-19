# Seinfeldvision Runway Model

<a href="http://sdk.runwayml.com" target="_blank"><img src="https://runway.nyc3.cdn.digitaloceanspaces.com/assets/github/runway-badge.png" width=100/></a>

This is a [GPT-2](https://github.com/openai/gpt-2) (345M) model that was trained on a corpus of Seinfeld scripts I scraped from [http://www.seinfeldscripts.com](http://www.seinfeldscripts.com). **I don't know if I have the right to use it, and consequently, I don't know if you have the rights to use this**. Hence, I won't add this corpus here, only the model.

I used the [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) package to download and re-train the model. You can do the same by following the details in these google colab notebooks:

1. [01_get-seinfeld-corpus](data_preparation_notebooks/01_get-seinfeld-corpus.ipynb)
2. [02_Train-a-GPT-2-Text-Generating-Model-w-GPU.ipynb](data_preparation_notebooks/02_Train-a-GPT-2-Text-Generating-Model-w-GPU.ipynb) - this is straight up copied from [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple). Good work, [@minimaxir](https://github.com/minimaxir)!.

---

## The trained model

The GPT-2 345M model takes approximately 1.5GB on disk. Github won't let you upload such a large file, so I put it [here](http://116.203.128.238/checkpoint.tar.gz)\*. The runway app is configured to download it automatically for you, but installation might take a few minutes longer because of this external download.

## Inputs and outputs

The model accepts a text input, which it sets as the context for the seinfeld dialogue to be generated in.

## How to use in the Runway app

TODO

## Examples

TODO


---

No rights ever held 2019, @jonathanronen

\* I don't promise this link will stay up for any length of time

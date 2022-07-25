from docxtpl import DocxTemplate
from Pyscipaper.abstract import abstract
from Pyscipaper.results import results
from Pyscipaper.discussion import discussion
from Pyscipaper.introduction import introduction
from Pyscipaper.methods import methods
from Pyscipaper.legends import legends

# to work with citations use {Abi-Saab, 1999 #888}. This solution will work with Endnote.

root = "/alzheimer/Roberto"
doc = DocxTemplate(f"{root}/Pyscipaper/Manuscript_template.docx")


title = "Differential ripple propagation along the hippocampal longitudinal axis"
authors = "Roberto De Filippo¹? and Dietmar Schmitz¹?"
affiliations = "¹? Charité? Universitä?tsmedizin Berlin, corporate member of Freie Universitä?t Berlin, Humboldt-Universitä?t" \
               " zu Berlin,and Berlin Institute of Health; Neuroscience Research Center, 10117 Berlin, Germany"
correspondence_to = "roberto.de-filippo@charite.de and dietmar.schmitz@charite.de"
keywords = "Hippocampal ripples, Ripples propagation, Anisotropy"

acknowledgements = "This work was supported by the Bundesministerium for Bildung und Forschung (SFB1315-327654276) grant.  " \
                "We thank J.T. Tukker, N. Maier for feedback on an early version of the manuscript. " \
                "The authors declare that they have no competing interests. "

contributions = "Conceptualization, data curation, formal analysis, investigation, visualization:  RDF. Writing - original draft: RDF. " \
                "Writing - review & editing: RDF, DS. " \
                "Funding acquisition: DS."

data_availability = "All the code used to process the dataset is available at https://github.com/RobertoDF/De-Filippo-et-al-2022, pre-computed data structures "\
                    "can be downloaded at 10.6084/m9.figshare.20209913.  "\
                    "All figures and text can be reproduced using code present in this repository, each number present in the text is directly "\
                    "linked to a python data structure. The original dataset is provided by the Allen Institute and available at "\
                    "https://allensdk.readthedocs.io/en/latest/visual_coding_neuropixels.html."

context = {'title': title, "authors": authors, "affiliations": affiliations, "correspondence_to": correspondence_to,
           "keywords": keywords, "abstract": abstract, "introduction": introduction,
           "discussion": discussion, "methods": methods, "results": results, "legends": legends, "acknowledgments": acknowledgements,
           "contributions": contributions, "data_availability": data_availability}

doc.render(context)
doc.save(f"{root}/Pyscipaper/De Filippo et al., 2022.docx")


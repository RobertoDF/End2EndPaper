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

title = "5-HT effect on human hippocampal ripples"
authors = "Roberto De Filippo¹ and Dietmar Schmitz¹"
affiliations = "¹ Charité Universitätsmedizin Berlin, corporate member of Freie Universität Berlin, Humboldt-Universität" \
               " zu Berlin,and Berlin Institute of Health; Neuroscience Research Center, 10117 Berlin, Germany"
correspondence_to = "roberto.de-filippo@charite.de and dietmar.schmitz@charite.de"
keywords = "Hippocampal ripples, 5-HT"


context = {'title': title, "authors": authors, "affiliations": affiliations, "correspondence_to": correspondence_to,
           "keywords": keywords, "abstract": abstract, "introduction": introduction,
           "discussion": discussion, "methods": methods, "results": results, "legends": legends}
doc.render(context)
doc.save(f"{root}/Pyscipaper/De Filippo et al., 2022.docx")


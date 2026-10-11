# BLD_26_40 — Building Renovation Cost and CO₂ Estimation Tool

## Table of Contents

- [Project Overview](#project-overview)
- [A2a — About the Group](#a2a--about-the-group)
- [A2b — Identifying the Claim](#a2b--identifying-the-claim)
- [A2c — Use Case](#a2c--use-case)
- [A2d — BPMN Diagram](#a2d--bpmn-diagram)
- [A2e — Description of the BPMN Workflow](#a2e--description-of-the-bpmn-workflow)
- [A2f — Information Requirements](#a2f--information-requirements)
- [References](#references)

---

## Project Overview

This project aims to develop a tool that estimates the costs and CO₂ emissions associated with newly added building elements in renovation projects.

The tool uses Building Information Modelling (BIM) and Industry Foundation Classes (IFC) models to extract relevant building information, including element types, materials, quantities, areas, and volumes. This information is combined with predefined price and CO₂ emission dictionaries to estimate the economic and environmental impacts of different renovation alternatives.

The project compares one original building model with three renovation models developed by other students. The focus is exclusively on newly added elements; removed elements are excluded from the cost and CO₂ calculations.

The ultimate goal is to provide clients and building professionals with a clear overview of the estimated costs and environmental impacts of different renovation solutions, supporting more informed and sustainable design decisions.

## A2a — About the Group

**Python confidence level: 2 — Basic knowledge**

The group has a basic understanding of Python and fundamental programming concepts. We can write and adapt simple Python code, but we have limited experience with advanced programming.

**Focus area:** Building

## A2b — Identifying the Claim

### Selected Building Models

The following structural building models were selected:

- Building #2602 (STR)
- Building #2606 (STR)
- Building #2609 (STR)

We selected the STR files because our project focuses on structural building elements, such as walls, beams, columns, and slabs. The other available files do not provide the same relevant structural information for our intended analysis.

### Claim

Develop a tool that provides clients with an overview of the estimated costs and CO₂ emissions associated with the materials used in renovated building elements, such as walls, beams, columns, and slabs.

### Justification

Sustainability and economic considerations are increasingly important during the design and renovation phases of building projects. Providing an early overview of material costs and CO₂ emissions can help clients and building professionals compare different design options and make more informed decisions.

Integrating these two aspects into a single tool can support the selection of more cost-effective and environmentally sustainable solutions.

## A2c — Use Case

### How would you check this claim?

We would first test the tool using simple building models containing basic elements such as walls, beams, columns, and slabs. The tool would extract the relevant quantities from the BIM models and combine them with predefined cost and CO₂ emission data.

The results would then be compared with manually calculated estimates to verify that the tool provides accurate and consistent results. Once the tool works correctly with simple models, it can be tested on more complex renovated building models.

### When would this claim need to be checked?

The claim would need to be checked once the BIM models from the different designers have been submitted and are sufficiently developed to provide reliable information about building elements and materials.

This would allow the tool to generate cost and CO₂ estimates based on the actual design information.

### What information does this claim rely on?

The tool relies on the following information:

- **BIM/IFC model information:** Element types, quantities, dimensions, areas, volumes, and material properties.
- **Price dictionary:** Unit prices associated with the relevant materials and building elements.
- **CO₂ emissions dictionary:** CO₂ emission factors associated with the relevant materials.

These inputs allow the tool to estimate the economic and environmental impacts of the renovation alternatives.

### What phase is this claim relevant to?

The claim is mainly relevant during the planning and design phases, particularly when different renovation options can still be compared and modified.

The tool can help clients evaluate the economic and environmental impacts of design choices before construction begins.

### What BIM purposes are required?

The main BIM purposes are **Gather, Analyse, and Communicate**.

- **Gather:** Collect quantities, materials, and building-element information from the BIM models.
- **Analyse:** Compare the original and renovated models, identify newly added elements, and calculate their estimated costs and CO₂ emissions.
- **Communicate:** Present the results clearly to clients and designers to support decision-making.

### Review of Existing BIM Use Cases

Reference: [Use Cost Estimation — BIM Project Execution Planning](https://psu.pb.unizin.org/bimprojectexecutionplanning/back-matter/use-cost-estimation/)

As mentioned by Tim, some of the traditional BIM use cases that we saw on the course website as examples can be considered somewhat outdated, as many of these processes existed before modern BIM technology. However, they can still be useful depending on the project. In our case, we can use Quantify, Analyse, and Author Cost Estimate since our model compares an original model with three renovation models made by other students. In our model we focus on identifying only the newly added elements and calculating their costs and CO₂ emissions based on what type of element has been added (without including removed elements). Although the existing use cases do not fully cover our models purpose, by combining them will allow us to evaluate the economic impact as well as the enviromental of different renovation solutions.

## A2d — BPMN Diagram

The following BPMN diagram illustrates the workflow of our tool, from importing the original and renovated IFC models to estimating costs and CO₂ emissions and presenting the final results.

![BPMN Workflow](A2/IMG/A2_diagram.svg)


## A2e — Description of the BPMN Workflow

The BPMN diagram represents the workflow of a tool developed to estimate the costs and CO₂ emissions associated with materials used in renovated building elements, including walls, doors, windows, slabs, beams, and columns.

The objective is to provide clients with a clear overview of the economic and environmental impacts of different renovation alternatives.

### 1. Reference Inputs

The process requires three main inputs:

- **Original and renovated building models:** One original building model and three renovated models — Building #2602 (STR), Building #2606 (STR), and Building #2609 (STR) — provided by the designers.
- **Price dictionary:** A dictionary developed by a previous student group, which will be reused to obtain the unit prices required for cost estimation.
- **CO₂ emissions dictionary:** A dictionary containing the relevant CO₂ emission factors for the materials.

### 2. Import and Identification of Building Elements

The process starts by importing the original and renovated IFC models. The tool then identifies and counts the relevant building elements in each model, including walls, doors, windows, slabs, beams, and columns.

The models are compared to identify the elements that have been added or removed during renovation. This comparison provides the basis for evaluating the changes introduced by each renovation alternative.

### 3. Internal Verification of the Results

After identifying the building elements, the tool checks whether the extracted element counts are acceptable.

At this stage, an Excel file is generated showing the elements in the original building and the numbers of elements added and removed in each renovated model.

This file is used exclusively for internal verification. It allows the group to check whether the IFC models have been interpreted correctly and whether the comparison between the original and renovated models is accurate. It will not be submitted to the client.

If the results are not acceptable, the process returns to the problem-identification stage so that potential errors can be investigated and corrected.

### 4. Cost Estimation

Once element identification and verification have been completed, the tool assigns the corresponding unit prices to the relevant newly added elements or materials.

The price dictionary, provided as a `.txt` file and developed by the previous group, is used to retrieve the appropriate unit prices. These prices are combined with the quantities extracted from the IFC models to calculate the estimated cost of the elements added to each renovated building model.

Removed elements are excluded from the final cost estimation.

### 5. CO₂ Emissions Estimation

Following the cost estimation, the tool assigns the corresponding CO₂ emission factors to the relevant elements or materials using the CO₂ emissions dictionary, also provided as a `.txt` file.

The tool then calculates the estimated CO₂ emissions associated with the elements added to the renovated models.

### 6. Validation of the Final Results

The calculated cost and CO₂ results are checked to ensure that they are consistent and acceptable. This includes verifying that every relevant element has been assigned an appropriate price and CO₂ emission factor and that the calculations have been performed correctly.

If inconsistencies are detected, the process returns to the problem-identification stage so that the issues can be investigated and corrected.

If the results are acceptable, the process continues to the final output.

### 7. Final Output for the Client

The final validated results are presented in an Excel file containing the estimated costs and CO₂ emissions associated with the elements added to the renovated building models, together with relevant information about the original building.

Unlike the first Excel file, which is used only for internal verification, this final output is intended to be communicated to the client.

It provides an overview of the estimated economic and environmental impacts of each renovation alternative and supports decision-making when comparing different renovation solutions.

## A2f — Information Requirements

For our project and model code, we extract information from four IFC models: one original model ( the OG model)  and three different renovation models made by other students from the previous semester. For our model we only focus on the newly added elements, as removed elements will not be included in our cost and CO₂ calculations.
The information we excract from the IFC models are different elements, here being  element types, materials, quantities, areas, and volumes. Depending on what element we are dealing with, its material etc we will have a rough pricelist of how much for example each square meter of a simple inner wall would cost. 
To calculate the environmental and economic impact, we will similarly with the price list make a CO₂ emission list in a similar fashion. These values may not be included in the IFC models, meaning we might need to collect them from external databases or make estimations.
We plan to use Python and ifcOpenShell to extract and compare the information from the four models. However, we still need to learn how to access the relevant IFC properties, identify added elements accurately, and organise and make sure the model properly extracts the needed information for it to be able to happen.
The final goal is to create a comparison of the three renovation alternatives based on the quantity of new materials, their estimated costs, and their environmental impact in terms of CO₂ emissions. This will help us evaluate the differences between the renovation solutions.

## References

1. [Assignment A2 — Tim McGinley](https://timmcginley.github.io/41934/Assignments/A2.html)
2. [Use Cost Estimation — BIM Project Execution Planning](https://psu.pb.unizin.org/bimprojectexecutionplanning/back-matter/use-cost-estimation/)

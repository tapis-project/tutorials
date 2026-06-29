# TPC26 Tapis Tutorial

## Tutorial Materials

<div class="callout callout-info">
  <strong>Tutorial Slides</strong><br/>
  <a href="https://docs.google.com/presentation/d/1s7S295ntrG8ZBu67HUuwjj9trcZz1pBsC57D6t5CIkE/edit?slide=id.p1#slide=id.p1" target="_blank">Slides for this tutorial</a><br/><br/>
📝 <strong>Reservation Info</strong><br/>
<strong>Allocation Code:</strong> <code>TRA24006</code><br/>
<strong>Sunday sessions:</strong> <code>Tapis+Tutorial-Sun</code><br/>
<strong>Monday sessions:</strong> <code>Tapis+Tutorial-Mon</code>
</div>


## Trillion Parameter Consortium 2026 Tutorial Schedule

Day 1 (May 31st) Schedule 

| Time         | Duration | Description                                                                                                                    | Speaker             |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| 2:00-3:00 PM | 60 min   | (Lecture) [Section 1: AI/ML, the National CyberInfrastructure Ecosystem and Tapis](./Intro_Tapis/01-intro-to-tapis.md)         | Anagha Jamthe       |
| 3:00-3:30 PM | 30 min   | (Hands-on) [Section 2: Initial Steps With TapisUI](./Intro_Tapis/02-initial-tapis-ui.md)                                       | Christian R. Garcia |
| 3:30-4:00 PM | 30 min   | Coffee Break                                                                                                                   |                     |
| 4:00-4:45 PM | 45 min   | (Lecture) [Section 3: Modern AI, Scientific Workflow and Infrastructure Gaps, Tapis Solutions](./Tapis_FlexServ/01-lecture.md) | Wei Zhang           |
| 4:45-5:30 PM | 45 min   | (Hands-on) [Section 4: Running AI Inference on Vista Via Tapis and FlexServ](./Tapis_FlexServ/01b-running-flexserv.md)         | Wei Zhang           |
  
Day 2 (June 1st) Schedule 

| Time           | Duration | Description                                                                                                                             | Speaker             |
| -------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| 9:00-9:30 AM   | 30 min   | (Lecture) [Section 5: Computer Vision Models in Scientific Applications](./Vision_Models/01-intro-vision-models.md)                     | Christian R. Garcia |
| 9:30-10:00 AM  | 30 min   | (Lecture + Hands-on) [Section 6: Fine-tuning the Vision Model with Ultralytics and Tapis](./Fine_Tuning_Vision/01-intro-fine-tuning.md) | Anagha Jamthe       |
| 10:00-10:15 AM | 15 min   | (Hands-on) [Section 7: Launching Jupyter Notebook](./Jupyter-Notebook/intro-to-jupyter.md)                                              | Christian R. Garcia |
| 10:15-10:30 AM | 15 min   | (Lecture) [Section 8: Prompt-Engineering: Best Practices](./Vision_Models/02-prompt-engineering.md)                                     | Anagha Jamthe       |
| 10:30-11:00 AM | 30 min   | Coffee Break                                                                                                                            |                     |
| 11:00-11:30 AM | 30 min   | (Hands-on) [Section 9: Generating Code for a Vision Task and Executing in Jupyter](./Tapis_FlexServ/01c-code-gen-flexserv.md)           | Wei Zhang           |
| 11:30-12:00 PM | 30 min   | (Hands-on) [Section 10: Evaluating fine-tuned model within Jupyter](./Fine_Tuning_Vision/02-evaluation.md)                              | Wei Zhang           |
| 12:00-12:30 PM | 30 min   | Additional Use Cases and Discussion                                                                                                     | Christian R. Garcia |




The resources you will be using today are provided by funding from the National Science Foundation.

## Intro to Tapis 
* [Intro to Tapis](./Intro_Tapis/01-intro-to-tapis.md)


## Tapis Frequent Questions

<details>
<summary><strong>What is Tapis?</strong></summary>

Tapis is an NSF-funded API platform for managing high-performance computing (HPC) systems, running jobs, and managing data across HPC centers. Tapis allows users to manage compute resources, submit jobs, manage files through APIs or TapisUI.

</details>

<details>
<summary><strong>What is Flexserv?</strong></summary>

Flexserv is a Tapis service that allows you to deploy and serve AI/ML models on HPC or VM resources. It provides inference endpoints and a graphical interface for managing the service.

</details>


<details markdown="1">
<summary><strong>Where can I ask questions after the tutorial?</strong></summary>

* **During the tutorial:** Raise your hand and a taccster will come help you.
* **After the tutorial:** Open a ticket at [https://portal.tacc.utexas.edu/tacc-consulting](https://portal.tacc.utexas.edu/tacc-consulting) or post in the [Tapis Slack community](null).
* **GitHub issues:** For bugs or feature requests, visit [https://github.com/tapis-project](https://github.com/tapis-project).

</details>


## Links & Documentation

<div class="doc-grid">
  <div class="doc-grid-item">
    <a href="https://public.tapis.io" target="_blank">TapisUI — public tenant (public.tapis.io)</a>
    <a href="https://public.tapis.io" target="_blank"><img src="/tutorials/assets/tapisui_home.png" alt="TapisUI Dashboard"></a>
  </div>
  <div class="doc-grid-item">
    <a href="https://tapis-project.github.io/live-docs" target="_blank">Live Documentation of OpenAPI V3 Specs for all Tapis Services</a>
    <a href="https://tapis-project.github.io/live-docs" target="_blank"><img src="/tutorials/assets/livedocs.png" alt="Tapis Live-Docs"></a>
  </div>
  <div class="doc-grid-item">
    <a href="https://tapis.readthedocs.io/en/latest" target="_blank">Full documentation and guides for using Tapis</a>
    <a href="https://tapis.readthedocs.io/en/latest" target="_blank"><img src="/tutorials/assets/docs.png" alt="Tapis Documentation"></a>
  </div>
  <div class="doc-grid-item">
    <a href="https://tapis.readthedocs.io/en/latest/technical/tapisui.html" target="_blank">TapisUI specific documentation page</a>
    <a href="https://tapis.readthedocs.io/en/latest/technical/tapisui.html" target="_blank"><img src="/tutorials/assets/docstapisui.png" alt="TapisUI Documentation"></a>
  </div>
</div>

## More Information on Tapis Services:
* [Tapis Systems](https://tapis.readthedocs.io/en/latest/technical/systems.html)
* [Tapis Apps](https://tapis.readthedocs.io/en/latest/technical/apps.html)
* [Tapis Jobs](https://tapis.readthedocs.io/en/latest/technical/jobs.html)

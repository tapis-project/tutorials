# TPC26 Tapis Tutorial

## Trillion Parameter Consortium 2026 Tutorial Schedule

<a href="https://docs.google.com/presentation/d/1s7S295ntrG8ZBu67HUuwjj9trcZz1pBsC57D6t5CIkE/edit?slide=id.p1#slide=id.p1" target="_blank">Slides for this tutorial are here.</a>

Day 1 (May 31st) Schedule 
<style>
img {
  box-shadow: 0 0 .7rem rgba(0, 0, 0, 0.5);
}

.schedule-table th:nth-child(1),
.schedule-table td:nth-child(1) {
  white-space: nowrap;
  min-width: 6rem;
}
.schedule-table th:nth-child(2),
.schedule-table td:nth-child(2) {
  white-space: nowrap;
  min-width: 6rem;
}
</style>

| Time | Duration | Description |
|------|----------|-------------|
| 2:00-3:00 PM | 60 min | (Lecture) [Section1: AI/ML, the National CyberInfrastructure Ecosystem and Tapis](./Intro_Tapis/01-intro-to-tapis.md) |
| 3:00-3:30 PM | 30 min | (Hands-on) [Section 2: Initial Steps With TapisUI](./Intro_Tapis/02-initial-tapis-ui.md) |
| 3:30-4:00 PM | 30 min | Coffee Break |
| 4:00-4:45 PM | 45 min | (Lecture) [Section 3: Classes of AI Models, 3rd Party Model Registries, Flexserv](./Tapis_FlexServ/01-lecture.md) |
| 4:45-5:30 PM | 45 min | (Hands-on) [Section 4: Executing Large Models on Vista Via Tapis and Flexserv](./Tapis_FlexServ/01b-running-flexserv.md) |
  
Day 2 (June 1st) Schedule 
<style>
img {
  box-shadow: 0 0 .7rem rgba(0, 0, 0, 0.5);
}

.schedule-table th:nth-child(1),
.schedule-table td:nth-child(1) {
  white-space: nowrap;
  min-width: 6rem;
}
.schedule-table th:nth-child(2),
.schedule-table td:nth-child(2) {
  white-space: nowrap;
  min-width: 6rem;
}
</style>

| Time | Duration | Description |
|------|----------|-------------|
| 9:00-9:30 AM | 30 min | (Lecture) [Section 5: Computer Vision Models in Scientific Applications](./Vision_Models/01-intro-vision-models.md) |
| 9:30-10:00 AM  | 30 min   | (Lecture) <a href="https://docs.google.com/presentation/d/1s7S295ntrG8ZBu67HUuwjj9trcZz1pBsC57D6t5CIkE/edit?slide=id.g3cd6a51b6a2_0_42#slide=id.g3cd6a51b6a2_0_42" target="_blank">Fine-tuning the Vision Model with Ultralytics and Tapis Part 1</a> <br/> (Hands-on) [Fine-tuning the Vision Model with Ultralytics and Tapis Part 2](./Fine_Tuning_Vision/01-intro-fine-tuning.md) |
| 10:15-10:30 AM | 15 min | (Lecture) [Prompt-Engineering: Best Practices](./Vision_Models/02-prompt-engineering.md) |
| 10:30-11:00 AM | 30 min | Coffee Break |
| 11:00-11:30 AM | 30 min | (Hands-on) [Generating Code for a Vision Task and Executing in Jupyter](./Tapis_FlexServ/01c-code-gen-flexserv.md) |
| 11:30-12:00 PM | 30 min | (Hands-on) [Evaluating fine-tuned model within Jupyter](./Fine_Tuning_Vision/02-evaluation.md)|
| 12:00-12:30 PM | 30 min | Additional Use Cases and Discussion |


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


<details>
<summary><strong>Where can I ask questions after the tutorial?</strong></summary>

* **During the tutorial:** Raise your hand and a taccster will come help you.
* **After the tutorial:** Open a ticket at [https://portal.tacc.utexas.edu/tacc-consulting](https://portal.tacc.utexas.edu/tacc-consulting) or post in the [Tapis Slack community](null).
* **GitHub issues:** For bugs or feature requests, visit [https://github.com/tapis-project](https://github.com/tapis-project).

</details>


## Links & Documentation
[The tutorial covers TapisUI in the public tenant: public.tapis.io](https://public.tapis.io)

[![TapisUI Dashboard](/tutorials/assets/tapisui_home.png){:style="max-width:50%;"}](https://public.tapis.io){:target="_blank"}

[Live Documentation of OpenAPI V3 Specs for all Tapis Services](https://tapis-project.github.io/live-docs)

[![Tapis Live-Docs](/tutorials/assets/livedocs.png){:style="max-width:50%;"}](https://tapis-project.github.io/live-docs){:target="_blank"}

[Full documentation and guides for using Tapis](https://tapis.readthedocs.io/en/latest)

[![Tapis Documentation](/tutorials/assets/docs.png){:style="max-width:50%;"}](https://tapis.readthedocs.io/en/latest){:target="_blank"}

[TapisUI specific documentation page](https://tapis.readthedocs.io/en/latest/technical/tapisui.html)

[![TapisUI Documentation](/tutorials/assets/docstapisui.png){:style="max-width:50%;"}](https://tapis.readthedocs.io/en/latest/technical/tapisui.html){:target="_blank"}

## More Information on Tapis Services:
* [Tapis Systems](https://tapis.readthedocs.io/en/latest/technical/systems.html)
* [Tapis Apps](https://tapis.readthedocs.io/en/latest/technical/apps.html)
* [Tapis Jobs](https://tapis.readthedocs.io/en/latest/technical/jobs.html)

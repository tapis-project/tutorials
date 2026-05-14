# Enabling Reproducible AI Workflows for the NAIRR Ecosystem

## NAIRR 2026 Tutorial Schedule

[Slides for this tutorial are here.](https://docs.google.com/presentation/d/1BVLnUbyiWjsaS33zMshW3TXqtfvv6zGklaCNBeX7Go0/edit?usp=sharing)

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
| 9:00-10:00 AM | 60 min | (Lecture) [AI/ML, the National CyberInfrastructure Ecosystem and Tapis](./Intro_Tapis/01-intro-to-tapis.md) |
| 10-10:30 AM | 30 min | (Hands-on) [Initial Steps With TapisUI](./Intro_Tapis/02-initial-tapis-ui.md) |
| 10:30-11 AM | 30 min | Coffee Break |
| 11-11:45 AM | 45 min | (Lecture) [Classes of AI Models, 3rd Party Model Registries, Flexserv](./Tapis_FlexServ/01-lecture.md) |
| 11:45-12:30 PM | 45 min | (Hands-on) [Executing Large Models on Vista Via Tapis and Flexserv](./Tapis_FlexServ/01b-running-flexserv.md) |
| 12:30-1:30 PM  | 60 min | Lunch  |
| 1:30-2:00 PM | 30 min | (Lecture) [Computer Vision Models in Scientific Applications](./Vision_Models/01-intro-vision-models.md) |
| 2:00-2:15 PM | 15 min | (Hands-on) [Launching Jupyter Notebook](./Jupyter-Notebook/intro-to-jupyter.md) |
| 2:15-2:45 PM | 30 min | (Lecture) [Prompt-Engineering: Best Practices](./Vision_Models/02-prompt-engineering.md) <br/>(Hands-on) [Generating Code for a Vision Task and Executing in Jupyter](./Tapis_FlexServ/01c-code-gen-flexserv.md) |
| 2:45-3:00 PM | 30 min | (Lecture + Hands-on) [Fine-tuning the Vision Model with Ultralytics and Tapis](./Fine_Tuning_Vision/01-intro-fine-tuning.md) |
| 3:00-3:30 PM | 30 min | Coffee Break |
| 3:30-4:15 PM | 45 min | (Hands-on) [Re-evaluating Using best.pt within Jupyter](./Fine_Tuning_Vision/02-evaluation.md) |
| 4:15-5:00 PM | 45 min | Additional Use Cases and Discussion |

<!-- | 3:30-3:50 PM | 20 min | (Lecture) Fine-tuning a Vision Model with Ultralytics |
| 3:40-4:00 PM | 10 min | (Hands-on) Submitting a Fine-tuning job via TapisUI | -->


The resources you will be using today are provided by funding from the National Science Foundation.

## Intro to Tapis 
* [Intro to Tapis](./Intro_Tapis/01-intro-to-tapis.md)
 

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

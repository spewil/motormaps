---
author:
- spencer wilson
title: virtual motor control [draft \today]
fontfamily: sans
geometry:
- margin=.75in
---

<!-- ## Background / Prior Art

## Question / Problem / Confusion

## Hypothesis

## Experiments / Test / Necessary Data

## Model / Mechanism -->

## Overview / Goals

```python
for i in range(10):
	pass
```

From _Takei et al. 2017_:

> It is generally believed that the direct corticomotoneuronal (CM) pathway, which is a phylogenetically newer pathway in higher primates, plays a critical role in the fractionation of muscle activity during dexterous hand movements. However, the present study demonstrated that PreM-INs, which are phylogenetically older, have spatiotemporal properties that correlate with muscle synergies during voluntary hand movements. Therefore, it is likely that these two systems have specialized functions for the control of primate hand movements, namely “fractionated control” and “synergistic control,” respectively. [...] Our results suggest that the phylogenetically older premotor interneuron system provides synergistic control of hand movements upon which the newer corticomotoneuronal system superimposes more fractionated control. [...] Optimization of balanced control may be an important factor also for the acquisition of new motor skills[@Takei2017].

Starting from this line of physiological work on descending outputs driving muscles of the hand and digits in higher primates, we aim to undertake a study that:

- explores the limitations of human motor output and learning
- develops mechanistic models of motor learning based on physiological evidence of the CST
- connects work on muscle synergies, corticomotoneuronal connections, and algorithms for motor control

The initial goal is to gain some insight into the question of the limitations of human motor learning as measured by the task dimensionality a human subject can achieve.

We plan to set up an experiment in which muscle output is mapped to a virtual task with various levels of dimensionality. We expect to find a limit on this dimensionality which is less than the available number dimensions, whether in muscles, motor units, or muscle synergies. We will then use our data to generate mechanistic interpretations of the sources of this dimensionality limit.

Specifically, our aim is to design a task where the control inputs are muscle activity of dimension $N$. Because we are interested in the behavioral relevance of CM connections, we choose these muscles to be of the hand and digits. We then design mappings from this control output to a virtual scene of dimension $M$. Thus, the task consists firstly in learning the mapping $f: \mathbb{R}^N \rightarrow \mathbb{R}^M$. There are obviously a large number of parameters for such a task, including:

- Mapping
    - linear
    - nonlinear (with tunable nonlinearity)
- Control mode
    - closed-loop (e.g. tracking, balancing)
    - open-loop (e.g. reach, point)
- Sensory feedback
	- auditory
	- visual
	- proprioceptive
	- cutaneous

Our hypothesis that relatively high dimensionality tasks can be learned in the distal muscles with increasing learning curve time constant. Additionally, we expect to discover synergetic muscle activations in higher dimensional tasks that prohibit further fractionation of motor outputs. A second, slower time constant, we hypothesize, will emerge at higher dimensional tasks that is limited by the reformulation of synergies. These time constants should underlie a multi-rate, hierarchical neural controller.

These types of control problems are something primates in particular are most adept at. We want to generate a systematic characterization of our ability to solve such control problems using the hands using recent physiological findings.

Such characterization, we think, will gain ground on the following questions:

- What are the strategies for learning novel motor tasks?
- Do our current models agree with such strategies? At the muscle level?
- Are we optimal? How so?
- What enables this (sub)optimality?
- What are the limits of human learning? (As opposed to the limits of motor output[@Scheiber2004])
- How can we best extend current theory of motor learning and control?
- Can our findings and models advance engineering motor learning and control _in silico_?

We hypothesize a particular purpose for CM connections in dealing with online error correction. Specifically, we should find suboptimal control to perturbations if synergies are fixed. We agree with the suggestion by Takei et al. that CM connections may underlie the fractionation of synergies. Perhaps this can be seen in response to an unexpected disturbance, when synergies would supply suboptimal motor responses.

Recording at the muscle allows us to relate the learning of novel mappings (and possibly new synergies) to dealing with online corrections. As far as we know, there is no prior work characterizing the difference between learning novel sensorimotor mappings which include perturbative elements. We see this as a rich avenue for mechanistic theory production.

There are a few tasks similar to what has just been described that are worth summarizing.

## Prior Relevant Tasks

There are several tasks from the literature worth highlighting. I have provided brief comments on each.

Structured Variability of Muscle Activations Supports the Minimal Intervention Principle of Motor Control [@Valero-Cuevas2009]

- We should investigate the difference between open-loop and closed-loop. This closed-loop control task showed little signs of synergies at the finger level.
- The single degree of freedom in the task as well as the reliance on force as the output does not test how we learn a new motor mapping, as we are producing a movement that we regularly generate, namely a single finger pushing down onto a surface.
- This highlights the difference between digit-based tasks and limb-based tasks
- How does the dimension of the synergy relate to the dimension of the task? This work argues that that are fundamentally linked.
- Using fine-wire electrodes, the study attempts to find activations of individual muscles using anatomical knowledge. This is obviously superior to inferring individual muscle activities using sEMG.


Differences in Adaptation Rates after Virtual Surgeries Provide Direct Evidence for Modularity [@Berger2013]

- Recorded from 13 arm and shoulder muscles, we expect results to differ for the digits
- Using a force calibration step limits the mappings that are available
- The incompatible rotation mappings are drastic (maps synergies to a single direction)


Remapping Hand Movements in a Novel Geometrical Environment[@Mosier2005]

- Learning a fixed mapping (18D “cyber glove” —> 2D cursor) for Euclidean Geometry
- Doesn't model or test algorithms for learning, only phenomenological
- No perturbative element to the task, a simple cursor movement
- No recording from the muscle level


Learning Optimal Adaptation Strategies in Unpredictable Motor Tasks[@Braun2009]

- There is an important distinction between adaptation and error correction
- Learning consists of control policy shift across trials-- in this case trials with visuomotor rotations.
- Error corrections use the same control policies, adaptation is a shifting of control policy to structurally learn task parameters (e.g. a new sensorimotor mapping). This is achieved by exposure to changes in task parameters which generate errors (mismatches between internal models and sensory evidence).
- We can ask whether this structural learning (probabilities of task parameters) is seen at the muscle level. We see that optimal adaptive control strategies seem to be achieved behaviorally, but how is this control achieved mechanistically by individual muscles.


Muscle Coordination Is Habitual Rather than Optimal [@DeRugy2012]

- Argues that though we see optimal control predict behavioral outcomes, at the level of the muscle we find synergies that are learned and difficult to overcome to achieve optimality per individual muscle. That is, subjects did not optimally overcome virtual alterations to their musculoskeletal outputs in an optimal manner, though evidence has been found to the contrary. However, this study, surprisingly, did not cite Valero-Cuevas et al. 2009.

<!-- The center of interest converges on a muscle-level description of the learning process of a novel mapping between muscle activity and a virtual scene.

The place to start is by using a force pad in place of the EMG signal to replicate behavioral studies. The force pad can be mapping to a virtual scene and data can be taken. This gives us a testing ground for investigating interesting mappings.

There are three concepts that tend to inhabit three separate realms in the literature:

- muscle synergies, particularly their flexibility and origin
- algorithms for motor control and learning, particularly optimal feedback control and the uncontrolled manifold hypothesis
- the physiology of the corticospinal tract, particularly corticomotoneuronal (CM) connections

I believe that by thinking about these disparate research topics as interconnected, we can learn something about the mechanisms by which humans are capable of quickly learning novel motor tasks. -->

## Towards a Model

Modeling the data from this work will:

- combine prior physiological and anatomical knowledge with behavioral evidence. The questions surrounding this element of a model are: optimality of behavior, the origins of versatility/dexterity in fine movements.
- explore the nature of synergies in fine motor tasks involving the hand. How does the motor system use synergies to learn new mappings while remaining robust to perturbations
- be hierarchical in nature to reflect knowledge about the CST and prior modeling efforts[@Todorov2005,Loeb2004].
- produce muscle-level predictions for a given mapping or family of mappings.

## Challenges

- How can recording at the muscle reliably reject/support a claim made about the brain? (This has been done exceedingly well in work by Wolpert and Shadmehr, for example.)
- How can we ensure that this work is impactful? Why does the trail to model motor control of the hand seem to have gone cold? Can we resurrect it with new physiological evidence?
- How do you find a synergy / motor map from surface EMG? Can we incorporate anatomical priors? A calibration process? We assume that such a calibration (e.g. handling a range of natural objects) process is made up of learned coactivations—is there a path, computational or experimental, towards separating individual muscles from these coactivations?
- One route is to simply generate a mapping based on anatomical knowledge and record the learning process. This will illuminate the possibilities for adaptation to a task outside of any functional synergies. However, this experiment would be even more illuminating if we first generated a map of synergies but recording users' interactions with various objects and tools. This has been done using "cybergloves" in the past, but not with EMG recording[@TodorovDimensionality2005,@Ingram2009].
- There are a few technical difficulties with muscle recording. First, comparing the "natural" correlations of muscle activations prior to learning a novel task requires either reconstruction of muscle covariance via ground truth data from the same task, though this requires the task being completed using some existing controller such as a force sensor. Second, using direct electromyographic control ostensibly negates the involvement of cutaneous feedback as one would have in a force-based task. Additionally, the role of proprioceptive feedback is unclear and open to questions.


<!-- ## CM Connections



There is work suggesting that CM connections synapse primarily on low threshold motor units that are recruited first. This would imply a difference in synergy fractionation at lower force as opposed to higher force. This can be tested by adding a force parameter within a task.



This hunch was bolstered specifically by the work of Takei et al. in their 2017 PNAS paper:

> It is generally believed that the direct corticomotoneuronal (CM) pathway, which is a phylogenetically newer pathway in higher primates, plays a critical role in the fractionation of muscle ac- tivity during dexterous hand movements. However, the present study demonstrated that PreM-INs, which are phylogenetically older, have spatiotemporal properties that correlate with muscle synergies during voluntary hand movements. Therefore, it is likely that these two systems have specialized functions for the control of primate hand movements, namely “fractionated control” and “synergistic control,” respectively. The interaction of these two putative control systems might be the source of the exceptional versatility of primate hand move- ments. For example, a power grip (e.g., gripping a hammer) is characterized by the predominant coactivation of hand muscles. It is known that power grip requires less involvement of the CM system, and therefore might result more from the PreM-IN system. Conversely, fine control of individual finger movements (e.g., control of a fingertip force of a single digit) requires higher fractionation of individual muscles and probably depends more on the CM system. Indeed, muscle synergies are not active during fine individual finger movements in some cases. Precision grip requires the fractionation of hand muscles as well as their coactivation, and thus might depend on cooperation of both the CM and PreM-IN systems. These examples suggest that the optimal balance of the two control systems may vary according to task requirements. Optimization of balanced control may be an important factor also for the acquisition of new motor skills. For example, Berger et al. demonstrated that learning a new movement that is compatible with existing muscle synergies occurs much more quickly than learning a movement requiring new muscle synergies. This implies that establishing, modifying, or masking muscle synergies requires more training. This might explain our everyday experience that highly fractionated movements require extensive practice (e.g., using chopsticks requires more extensive training than using spoons). This conceptual framework of balanced control systems may help future studies to clarify how our nervous system controls and acquires versatile hand functions. [@Takei2017]

This notion of an "old" and "new" motor cortex is not conceptual, but has been shown using viral tracing techniques [@Rathelot2009].

As I see it, the goal is to build a falsifiable model which takes into account the bipartite structure of M1 into account, and find tasks that ostensibly require the direct descending connections to fractionate learned synergies. In effect, the hypothesis to test is that CM connections override the "consolidated" patterns putatively generated via spinal circuitry.

Thus, this is a learning question, an experimental problem, and a modeling task rolled into one. We have a good hunch that is backed up by solid work. The question comes down to how much we can learn by recording as much muscle activity as we can and designing very clever tasks to test very clever models.

## Muscle Synergies

There is a longstanding debate about the origins of muscle synergies that strongly mirrors the nature-nuture debate. Are synergies learned or are they hardwired? If they're hardwired, what physiological subsystem contains this hardwiring? We don't need to take a side because there is clear evidence that humans overcome synergies to adapt their mottor outputs to solve novel tasks and overcome all types of changes in the motor loop (injury, fatique, prism goggles, etc.) via well-studied (in laboratory tasks at least) adaptation mechanisms [Helmholtz, Wolpert, Todorov, newer work on synergy shifts such as [@DeRugy2012,Berger2013]. The more interesting questions ask on what timescales and by what mechanisms does learning occur, and can we reverse engineer paradigms and tasks that improve the learning rate.

Note that there are a great number of tasks, and the case for synergies in the motor system cannot be answered simply. Here we are concerned with motions of the hand because we know that this is the endpoint of CM connections. There are many fewer tasks dealing with this system in particular. Most tasks deal with arm reaching, though the most highly cited synergy paper deals with a 1DOF kick [@DAvella2003].

From a 2009 review suggesting exactly the work that our hunch is leading us towards:

> First, analyses such as that performed by Valero-Cuevas et al. [42  ] and Kutch et al. [40  ] should be done across many different behaviors and a wider range of behavioral con- ditions to evaluate whether the structure in the variability of muscle activation patterns is consistent with the muscle synergy hypothesis. Although the analyses used in those experiments exploit some ideal features of finger control, similar experiments should be possible in other behaviors and would help address concerns about syner- gies arising from task constraints. Second, it should be possible to use synergies to explain suboptimal perform- ance of the CNS [70]. If the CNS has access to a limited set of synergies at a particular time based on the tasks that it currently is able to accomplish, this should suggest that some new tasks should be easier to perform than others [44 ]: if the muscle activation patterns required by the new task lay within the space defined by existing muscle synergies, learning the new task should be relatively easy. In contrast, if the required activations lay outside that space, then the learning should be more difficult and initial performance should be suboptimal. Designing such tasks requires an accurate musculoskeletal model along with knowledge of the existing muscle synergies which would make it possible to predict which tasks would be easy and which would be difficult to learn.

Additionally, the review authors provide an argument for a developmental basis of the synergies we find in EMG recordings:

> Rather than considering muscle synergies as reflecting a strategy for the simplification of control, we suggest that synergies might be considered in the larger context of the intimate interactions between the proper- ties of the musculoskeletal system and neural control strategies. In this context, muscle synergies could be considered as reflecting the statistics of the external world, acknowledging the fact that the external world also consists of the musculoskeletal system itself. In the same way that properties of natural scenes might influence the structure of the visual system, we suggest that statistics of the musculoskeletal system and external world might influence the structure of motor systems.

Note that the authors' second suggestion has been tested in a reaching task. The results concorded witht the hypothesis from the quoted review, as we would expect:

> After compatible virtual surgeries, a full range of movements could still be achieved recombining the synergies, whereas after incompatible virtual surgeries, new or modified synergies would be required. Adaptation rates after the two types of surgery were compared. If synergies were only a parsimonious description of the regularities in the muscle patterns generated by a nonmodular controller, we would expect adaptation rates to be similar, as both types of surgeries could be compensated with similar changes in the muscle patterns. In contrast, as predicted by modularity, we found strikingly faster adaptation after compatible surgeries than after incompatible ones.

However, seeing that the mapping between the recorded EMG and the output was a multilinear regression based on a calibration dataset which was grossly altered for the surgery, I do not find it surprising that the learning curves were different after the two surgeries.


## Corticomotoneuronal Connections

There are very few tasks dealing with the hand in particular. What type of task would test the hypothesis that CM connections act to fractionate synergies of the hand such that we can tune a parameter of the task to require more or less influence of these direct connections? We would like to ask a user to fractionate synergies of the hand to different levels.

This requires first mapping the intrinsic available dynamics of the hand per user.

We then would like to present fixed mappings between hand output (either through dirct muscle activity or through a controller such as a force pad).


## Motor Control at an Algorithmic Level

Wolpert:
> From laboratory learning to real-world learning. We now have a detailed understanding of the learning and control of a narrow range of tasks, including simple reaching tasks in which visuomotor and dynamics perturbations are applied. Although these tasks are amenable to analysis and modelling, they do not capture the full complexity of real-world motor control and it is not clear whether the learning models that are developed will generalize to tasks such as tying shoelaces or learning to skateboard. The study of sensorimotor control is fundamentally difficult because it deals with a dynamic, real-time control system that turns sensations and memory into action and vice versa. Given this complexity, it is understandable that the field has focused on a limited number of simplified tasks. However, expanding the range of tasks may help us deal with new challenges.

Optimal Feedback Control (Todorov):
> In our motor outputs, we attempt to reduce variability in task relevant dimensions over task-irrelevant ones by what we call the "minium intervention principle".

This was shown to occur at the muscle level in a single finger task [@Valero-Cuevas2009]. -->

$\pagebreak$

## Works Cited

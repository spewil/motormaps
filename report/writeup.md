---
author:
- Spencer Wilson
title: \centering Sensorimotor Control in Complex Virtual Environments \break [Proposal Draft \today]
fontfamily: sans
geometry:
- margin=1in
---

<!--

## Abstract

## Question / Problem / Goal

## Background / Prior Art / Lit Review

## Hypothesis

## Experiments / Test / Necessary Data / Task

## Model / Mechanism

-->

## Abstract

During naturalistic behavior, previously acquired priors are updated by processing the statistics of the current environment. This learning process occurs across multiple timescales to achieve the goals of an ongoing plan. To solve such problems, we suggest that the nervous system leverages approximations and heuristics to generate suboptimal, albeit acceptable, solutions. Classical laboratory tasks, such as reaching under perturbations, tend not to reflect the statistical richness of natural sensorimotor control and learning. This work aims to engineer tasks which incorporate large state spaces and complex statistics towards reverse-engineering our ability to acquire novel motor skills. In order to cope with such task complexity, these tasks will require the use of our most capable appendage— the hand.

## Overview

<!-- Neurophysiologist Jose Delgado once quipped

 > The technology for communication between brains and computers through the intact skin is already at our fingertips. -->

The human hand is a unique evolutionary invention that enables an unprecedented ability to manipulate objects. As such, the hands provide a window into the strategies humans use to discover and internalize the statistical regularities of the world around them, as well as the mechanisms by which they respond to unpredictable disruptions to their sensory surround. In this way, the hands provide a direct link with neural processing in the brain. This is not merely speculative; it has been shown that the monosynaptic descending outputs controlling the digits act in coordination with synergistic muscle activations of the hand to achieve control that is balanced between modularity and dexterity:

> It is generally believed that the direct corticomotoneuronal (CM) pathway, which is a phylogenetically newer pathway in higher primates, plays a critical role in the fractionation of muscle activity during dexterous hand movements. However, the present study demonstrated that PreM-INs, which are phylogenetically older, have spatiotemporal properties that correlate with muscle synergies during voluntary hand movements. Therefore, it is likely that these two systems have specialized functions for the control of primate hand movements, namely “fractionated control” and “synergistic control,” respectively. ... Our results suggest that the phylogenetically older premotor interneuron system provides synergistic control of hand movements upon which the newer corticomotoneuronal system superimposes more fractionated control. ... Optimization of balanced control may be an important factor also for the acquisition of new motor skills[@Takei2017, @Rathelot2009].

This leads us to question our understanding of how complex tasks are achieved by the hands through a mixture of synergistic and fractionated output. Understanding how these facts of motor physiology connect to higher order models of behavior requires an experiment which circumvents the added complications of limb biomechanics by mapping muscle output directly to a virtual task. This has precedent in what is known in the literature as electromyographic (EMG) control or "myocontrol". By analyzing the structure of an EMG time series directly, we can both build a model of behavior that tests hypotheses at the muscle level and leverage a higher-dimensional control signal to generate complex, interactive virtual environments.

Specifically, we aim to design a task where the control inputs are a muscle activity signal of dimension $N$. Because we are interested in the behavioral relevance of CM connections, we choose these muscles to be of the hand and digits. We then design mappings from this control output to a virtual scene with a task of dimension $M$. Thus, the task consists of learning the mapping $f: \mathbb{R}^N \rightarrow \mathbb{R}^M$.

This general scheme gives us the the ability to construct families of mappings with particular spatiotemporal correlation structure. Inspiration for such a task can be seen in Knoll et al. 2018, where the authors devised a naturalistic random walking visual stimulus that required minimal prior training [@Knoll2018]. The authors analyzed the eye movements of humans, macaques, and marmosets to find that the spatial and temporal kernels of their tracking behavior was in agreement with prior, trial-based paradigms and provided support for general principles underlying spatiotemporal visual integration across species. Our hope is to develop human motor tasks that align with this focus on naturalism and continuity to elucidate general principles in sensorimotor learning by allowing direct input in such an environment.

We can engineer spatial and temporal correlations in a sensorimotor mapping in several ways. We might generate a mapping with state-dependent parameters, such that exploring the task's state space also means exploring the mapping space. Similarly, we can infuse correlations across time into the mapping to incorporate a memory component into the task. Of course, in both of these paradigms uncertainty can be introduced in a controlled manner such that the state and time dependence of the mapping becomes stochastic under a certain distribution. This stochasticity could be stationary or nonstationary as a testing ground for different hypothetical strategies or optimal solutions to the task under specific assumptions.

Our main goal in this project is to investigate the strategies we use to actively acquire new, or adapt existing, internal models in complex dynamic environments to produce goal-directed motor outputs. In line with this goal, we also ask what approximations or heuristics do we leverage during this model acquisition process, and are these related to innate/learned priors at the muscle? Specifically, how does a balance between synergistic and "direct" control of hand muscles play a role in sensorimotor learning? By "strategy" here we refer to the ability in this task, as opposed to classical psychophysics based on discrete responses to a sets of stimuli, to actively sample the task environment in order to collect information about the control parameters of the system of interest. To our knowledge, there has no study to date exploring and modeling active sensing at the muscle level.

By extending laboratory tasks to continuous, naturalistic motor problems that span multiple timescales and large state spaces, we hope to build a picture of the constraints involved in sensorimotor learning and control. We aim to gain an understanding of the degree to which we are optimal in our solutions, and what mechanisms generate this suboptimality. We hope to ultimately provide new avenues for modeling sensorimotor learning and control that will, in turn, inform our ability to construct dexterous systems _in silico_.

\newpage

## Challenges

### Dimensionality of the Hand

- The hand has 29 joints and 34 muscles, though the dimensionality of natural hand movements is closer to 8 based on PCA analysis [@TodorovDimensionality2005, @Ingram2009]. We expect there to be some biomechanical constraints on hand output dimensionality, though we hypothesize that it is higher than 8 and lower than 23, which gives us a relatively large task space to work with for generating mappings.
- We expect to find a limit on this dimensionality which is less than the available number dimensions, whether in muscles, motor units, or muscle synergies. We can use our data to generate mechanistic interpretations of the sources of this dimensionality limit, whether is is due to habitual movement or neural constraints. We expect to see multiple timescales of learning underlying these processes.
- Constraints on hand movements are force-dependent, and the Henneman Size Principle is most clearly seen in deliberate force ramps. There are some arguments against the principle as a rule [@Basmajian1963, @Scheiber2004], arguing that constraints on individuated movements may be habitual rather than developmental. This is a highly contentious debate in the muscle synergy literature, and it is unclear if this is a feature or a bug for the aims of this project.
- One route to circumvent hand constraints is to simply generate a mapping based on anatomical knowledge and record the learning process. This will illuminate the possibilities for adaptation to a task outside of any functional synergies. However, this experiment would be even more illuminating if we first generated a map of synergies but recording users' interactions with various objects and tools. This has been done using "cybergloves" in the past, but not with EMG recording[@TodorovDimensionality2005,@Ingram2009].

### Electromyography

- How can recording at the muscle reliably reject/support a claim made about the brain? This has been done exceedingly well in work by Wolpert and Shadmehr, for example, so perhaps if our hypotheses are specific and well-scoped, we will not be troubled.
- How do you find a reliable synergy map from surface EMG? Can we incorporate anatomical priors? A calibration process? We assume that such a calibration (e.g. handling a range of natural objects) process is made up of learned coactivations—is there a known path, computational or experimental, towards separating individual muscles from these coactivations? Is it more than just non-negative matrix factorization? How much of a hurdle is this?
- There are a few technical difficulties with muscle recording. First, comparing the "natural" correlations of muscle activations prior to learning a novel task requires either reconstruction of muscle covariance via ground truth data from the same task, though this requires the task being completed using some existing controller such as a force sensor. Second, using direct electromyographic control ostensibly negates the involvement of cutaneous feedback as one would have in a force-based task. Additionally, the role of proprioceptive feedback is unclear.

## Relevant Prior Tasks

There are several tasks from the literature with similar aims and/or methods worth highlighting briefly here:

__Structured Variability of Muscle Activations Supports the Minimal Intervention Principle of Motor Control [@Valero-Cuevas2009]__

- 1DOF force trajectory tracing task while recording fine-wire electrodes in 7 muscles of the finger
- Analysis of muscle covariance supports minimum intervention principle
- The single degree of freedom in the task as well as the reliance on force as the output does not test how we learn a new motor mapping, as we are producing a movement that we regularly generate, namely a single finger pushing down onto a surface.
- We should investigate the difference between open-loop and closed-loop. This closed-loop control task showed little signs of synergies at the finger level.
- This highlights the difference between digit-based tasks and limb-based tasks
- How does the dimension of the synergy relate to the dimension of the task? This work argues that they are fundamentally linked.
- Using fine-wire electrodes, the study attempts to find activations of individual muscles using anatomical knowledge. This is obviously superior to inferring individual muscle activities using sEMG.

__Learning Optimal Adaptation Strategies in Unpredictable Motor Tasks[@Braun2009]__

- Structural learning task: reaching with unpredictable visuomotor perturbations
- There is an important distinction between adaptation and error correction
- Learning consists of control policy shift across trials-- in this case trials with visuomotor rotations.
- Error corrections use the same control policies, adaptation is a shifting of control policy to structurally learn task parameters (e.g. a new sensorimotor mapping). This is achieved by exposure to changes in task parameters which generate errors (mismatches between internal models and sensory evidence).
- We can ask whether this structural learning (probabilities of task parameters) is seen at the muscle level. We see that optimal adaptive control strategies seem to be achieved behaviorally, but how is this control achieved mechanistically by individual muscles.

__Occam's Razor in Sensorimotor Learning [@Genewein2014]__

- Subjects trace best-fit lines in 2D point clouds generated by two different models
- Statistics of two models are learned by trial and error
- Subjects prefer simpler models when point clouds can be fit equally well (up to MSE)
- Controls are using a mouse to choose models instead of tracing and correcting for spatial frequency of trajectories by augmenting the variance of the two models
- Nice example of a possible inferential rule, though not exactly "sensorimotor learning"?

__Differences in Adaptation Rates after Virtual Surgeries Provide Direct Evidence for Modularity [@Berger2013]__

- Myocontrol center-hold, reach out task
- Recorded from 13 arm and shoulder muscles, we expect results to differ for the digits
- Multiple linear regressions of each applied force component (using force sensor for ground truth) to generate functions between EMG and force. Subsequently they use the EMG output directly.
- Using a force calibration step limits the mappings that are available
- Generate compatible and incompatible mappings based on the null space of calculated muscle synergies
- Finds synergies using NMF
- The incompatible rotation mappings are drastic: maps synergies to a single direction

__Muscle Coordination is Habitual Rather than Optimal [@DeRugy2012]__

- Myocontrol of a 2DOF cursor for center-hold, reach out
- Uses a custom gradient descent method to match normalized muscle activity to vector-target error
- Anatomical mapping for electrode placement for wrist muscles
- Claims that suboptimal activations are made to achieve task goals due to learn coactivations
- Introduces noise and perturbations to the task
- Admits that longer timescale learning may allow optimal activations
- Argues that though we see optimal control predict behavioral outcomes, at the level of the muscle we find synergies that are learned and difficult to overcome to achieve optimality per individual muscle.
- That is, subjects did not optimally overcome virtual alterations to their musculoskeletal outputs in an optimal manner, though evidence has been found to the contrary. However, this study, surprisingly, did not cite Valero-Cuevas et al. 2009.


__Flexible Cortical Control of Task-Specific Muscle Synergies [@Nazarpour2012]__

- Myocontrol of a 2DOF cursor
- Recorded 5 or 6 muscles (anatomical) with the arm strapped to a flat table
- 2 muscles are used for control of a orthogonal directions in a 2D screen
- The object of the game is to move the cursor
- Visual perturbations are introduced
- Subjects show the ability to form new "task-specific" synergies
- Supports minimum intervention, but is this just a task strategy as opposed to a feature of the motor system?

__Learning a Novel Myoelectric Control Interface Task [@Radhakrishnan2008]__

- Myocontrol of a 2DOF cursor
- Maps 6 muscles (6) to directions that are intuitive (in line with “expected” movements) or nonintuitive (randomly selected, some rotated)
- Muscles are stimulated to add noise
- Hand muscles are preferred in the task (mentions likelihood of CM connections playing a role)

__Learning Algorithms for Human-Machine Interfaces [@Danziger2009]__

- Myocontrol of a virtual 2DOF planar linkage
- Pseudoinverse of four “corner” calibration vectors (predetermined hand postures)
- Pass angles through a nonlinear function to control a planar linkage
- This is interesting in and of itself. They don’t show the linkage to the user, and the user seems to show some prior about how the cursor should move as they don’t know about the nonlinear constraint…
- Shows (obviously) that recalculating the mapping frequently disrupts learning, while having smooth variation in the mapping in line with subject error aids in achieving goals
- A reminder to enforce smoothness of maps across parameter space

__Remapping Hand Movements in a Novel Geometrical Environment[@Mosier2005]__

- Learning a fixed mapping (18D “cyber glove” —> 2D cursor) for Euclidean Geometry
- 2DOF cursor target task
- Doesn't model or test algorithms for learning, only phenomenological
- No perturbative element to the task, a simple cursor movement
- No recording from the muscle level
- Four corner calibration, MP pseudoinverse mapping
- All hand postures map to one screen coordinate, but screen coordinates can map to multiple hand postures
- Screen is reachable by linear combinations of joint positions
- This redundancy is a direct outcome of the pseudoinverse not being unique, which is a direct output of there being more joint angles than screen coordinates
- A nice discussion about inversions, integrability, and suggestions for future, more complex, mappings
- Nonlinear transformations have problems with integrability when differential inversions are applied, so people have invented special integrable inverses… here they use a linear transformation, so there is a MP inverse that creates a “family” of configurations that map actuator space to task space.


$\pagebreak$

## Works Cited

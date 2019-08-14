## Outline
Main goal/question
	- the human motor system has evolved to enable fine manipulation of objects as seen in our use of a range of tools, while remaining adaptive to flexibly accommodate a changing environment full of unpredictable perturbations. This combination of learned predictive processing and flexible responsiveness to uncertainty is the hallmark of the human motor system. In order to robustly achieve such a wide set of goals to a high degree, what approximations are used to quickly adapt to new situations?
Physiological underpinnings
Modeling prior work
Task setup / data shape

## Goal / Question
- How do you (what (sampling) strategies do you use to) actively acquire new (or adapt existing) internal (forward/inferential/cognitive) models in high-dimensional, nonlinear, and/or continuous state spaces to produce goal-directed motor outputs?
- What (suboptimal) approximations/heuristics do we leverage during this process?
- How are these related to innate/learned priors?
- The statistics of the task space drive the representation of movement, but how do we utilize (or sample?) the statistics of the environment to efficiently produce movements that achieve task goals?
- Can we explore the priors we use to efficiently learn new sensorimotor mappings by engineering the statistics of a task? (@ virtual surgery work)

## Active Sensing
- Hierarchical Bayesian models -- what does this actually look like…?
- Information theoretic constraints -- how are these formalized? (maybe see Braun’s work)
- Could this lead to characterizing some information theoretic constraints on how we can learn new skills? How we use strategies to cope with this limitations?
- What strategies are used for learning, and how do they relate to the statistical structure of the task?

## Adversarial Mappings
- What sensorimotor mappings are nontrivially unlearnable? (Where trivially unlearnable would mean something that requires more processing than we are capable of by simple transduction, etc. Example?)
- Can we engineering mappings with temporal correlations? What are the limits of such an internal model of this dynamics?
- Is the mapping a dynamical system? What aspect of dynamical systems can we (not) represent and use in the brain?
- What is the difference between these two versions?
- How do we generate these structured mappings in a principled manner?
- Can we engineer “latent” structure in a sensorimotor mapping to characterize the constraints of a neural learning system?

## Task

- Not dependent on limb mechanics
	- Focused on muscles of the hand (for CM connections)
- intuitive (preferably without explanation (@Huk)
- Think about priors? E.g. remaining upright…
- Complex / Naturalistic / High-dimensional
- Perhaps it is generative based on state? So no two subjects experience the exact same environment
- Why hand muscles directly? This removes the transformation from brain to hand coordinates, we’re directly tapped into the muscle space to test the limits of what can be learned by direct motor output

Thinking about the hands in particular, which seem to have far fewer constraints computationally / behaviorally as the arm, how can we begin to connect motor learning control to a broader understanding of learning and control in general?
What do we mean when we say learning and control in the context of the hands, who seem to have more “freedom” than the other limbs.
That is, the hands can be utilized as an output of cognition over the arms, which are more constrained.

## Model
Bayesian active sensor for uncovering latent structure of a novel sensorimotor mapping
Primitives (Todorov, Ghahramani) / modularity
We know that there are synergies at some level (Takei 2017, Gizster and his frogs)
What are their limits? When do we overcome them? With the hands, but what does this help us explain, or how does know this system, or modeling it, help us make more naturally moving robots / soft systems?
These synergies arise for several reasons
Biomechanical constraints (trivial)
Statistical structure of environmental demands (task dimensionality / dynamics)
Hierarchy (example? Todorov?)
How to structure this?
Todorov has a two-step mapping-- input to sensors to high (hidden) to low to output
This hierarchy relies on the statistics of the environment in which learning takes place
Override / Exploration / Dexterity -- how does this arise?
How do we test for this?
How is this different from Nazapour?
An ability to remain open to unpredictable events?
Based on the statistical structure of the task world
How can we leverage this to develop some behavioral analysis of motor “modules” or some such solution to the task?
How can we generate an understanding of how movements are shaped by the statistics of the environments in which we move?
Can we engineer the statistics of tasks to probe how the brain attempts to learn in the face of uncertainty, and choose a motor output solution (out of many) that suits the system? Can we relate this to subject-specific differences?
We know motor memories have multiple timescales of decay that reflect the statistics of the environment / skill (Shadmehr, Bastian, Wolpert)
“we present experimental evidence that sensory uncertainty, which affects motor variability, instead of variability per se, determines learning speed during trial-by-trial random perturbations” (Kording 2016 Statistical Determinants)

The reverse engineering problem is cool-- we present the system with a problem to solve, and we keep giving it problems until we define the boundaries of what it can learn, not learn, learn well, learn not-so-well. We have to construct these tasks in such a way that they tell us something specific.

What makes a mapping learnable, and how does a system change to learn a new mapping?
What has evolution done to accommodate mappings while retaining (or evolving) flexibility / dexterity?
How does robotics try to deal with this?
The system is hierarchical-- it has overlapping motor pools, synergies, reflexes, direct cortical overriding signals. It seems that it has a higher amount of direct control the further distal you go in the human arm.
The dynamics of the types of tasks humans can learn to do our crazy-- so we have to give up modeling them and learn how the system adapts to produce these outputs without an explicit model-- where does the “model” live?
What types of internal models can you learn? Not learn?
The motor system seems to effectively solve difficult inverse problems-- how

Drill in on the types of mappings, classes of mappings, that are learnable-- this tells us something about how the brain is undergoing the learning/adaptation process. This is the learning question, and it gives us insight into a model for how the brain learns to adjust for error in it’s task. We can even study this simply with a force output to start.
The second question is what the muscles are doing during the learning problem, and tying this back to our knowledge of the physiology of the system. The problem here is not providing mere speculation on what’s happening under the hood, but generating testable hypotheses. This step also required being very careful about the data collection process in order to make sure we have data that is capable of supporting out hypotheses
The next step is to design perturbations, within the task and for the mapping, and detect, for a given mapping, whether synergies are re-recruited or if other mechanisms are used to accommodate for unpredictable perturbations.

Interesting that users found it frustrating to adjust the mapping after each trial block-- how can we continually shift the mapping to maintain constant learning, or show some metalearning?

Perhaps with nonlinear mappings there is no closed form control solution, but we are able to control the system with our bodies. Is understanding how the system is solved (quickly?) by biological neural control connected to how it might be solved using, say, a neural network?


## CM Connections

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

We then would like to present fixed mappings between hand output (either through direct muscle activity or through a controller such as a force pad).


## Motor Control at an Algorithmic Level

Wolpert:
> From laboratory learning to real-world learning. We now have a detailed understanding of the learning and control of a narrow range of tasks, including simple reaching tasks in which visuomotor and dynamics perturbations are applied. Although these tasks are amenable to analysis and modelling, they do not capture the full complexity of real-world motor control and it is not clear whether the learning models that are developed will generalize to tasks such as tying shoelaces or learning to skateboard. The study of sensorimotor control is fundamentally difficult because it deals with a dynamic, real-time control system that turns sensations and memory into action and vice versa. Given this complexity, it is understandable that the field has focused on a limited number of simplified tasks. However, expanding the range of tasks may help us deal with new challenges.

Optimal Feedback Control (Todorov):
> In our motor outputs, we attempt to reduce variability in task relevant dimensions over task-irrelevant ones by what we call the "minium intervention principle".

This was shown to occur at the muscle level in a single finger task [@Valero-Cuevas2009].

## Towards a Model

Modeling the data from this work will:

- combine prior physiological and anatomical knowledge with behavioral evidence. The questions surrounding this element of a model are: optimality of behavior, the origins of versatility/dexterity in fine movements.
- explore the nature of synergies in fine motor tasks involving the hand. How does the motor system use synergies to learn new mappings while remaining robust to perturbations
- be hierarchical in nature to reflect knowledge about the CST and prior modeling efforts[@Todorov2005,Loeb2004].
- produce muscle-level predictions for a given mapping or family of mappings.

<!-- The center of interest converges on a muscle-level description of the learning process of a novel mapping between muscle activity and a virtual scene.

The place to start is by using a force pad in place of the EMG signal to replicate behavioral studies. The force pad can be mapping to a virtual scene and data can be taken. This gives us a testing ground for investigating interesting mappings.

There are three concepts that tend to inhabit three separate realms in the literature:

- muscle synergies, particularly their flexibility and origin
- algorithms for motor control and learning, particularly optimal feedback control and the uncontrolled manifold hypothesis
- the physiology of the corticospinal tract, particularly corticomotoneuronal (CM) connections

I believe that by thinking about these disparate research topics as interconnected, we can learn something about the mechanisms by which humans are capable of quickly learning novel motor tasks. -->

## Task notes

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

- What are the limits of human learning? (As opposed to the limits of motor output[@Scheiber2004])
- How can we best extend current theory of motor learning and control?
- Can our findings and models advance engineering motor learning and control _in silico_?

We hypothesize a particular purpose for CM connections in dealing with online error correction. Specifically, we should find suboptimal control to perturbations if synergies are fixed. We agree with the suggestion by Takei et al. that CM connections may underlie the fractionation of synergies. Perhaps this can be seen in response to an unexpected disturbance, when synergies would supply suboptimal motor responses.

Recording at the muscle allows us to relate the learning of novel mappings (and possibly new synergies) to dealing with online corrections.

Apart from generating a family of sensorimotor mappings to be learned under spatial or temporal dependence and/or sttochasticity, we could imagine mapping the eletromyographic input to the control input of various dynamical control systems. In this way, we can understand what strategies a subject uses to explore the passive dynamics of an unknown system. This system identification process, however, may complicate the task beyond the the relevant questions.


## Andy
- Try and tighten up the first page -- have all your main points up front.
- pull the three bullet point aims on the first page into one overall question
- too broad at the moment.
	- outline the aim as to “connect work on muscle synergies, corticomotoneuronal connections and algorithms of motor control to explore the limitations of human motor output and learning and develop mechanistic models”
	- towards one question
- I would remove the list of parameters on the first page, potentially move it to the end where it could fit in the “challenges” section?
- The list of questions at the top of page two I think is again a bit too much. Try and limit this down to 2-3 of the questions you think we can really make headway on.
- The part about CM connections and online error corrections is a great thought. Is there much on this?
“..the purpose of CM connections is dealing with online error corrections”. “Purpose” seems to be leading the section in the direction of saying that CM connections exist to help deal with the perturbations..is this what you’re thinking?
- Perhaps a similar point is
	- synergies may be set up to reduce the computational power required to generate specific common movements, but this comes at a cost of online corrections. So, how does the nervous system deal with this?
- The Prior Relevant tasks section does require some knowledge of each study to make the best use of your points. A line stating what each study looked at/their task design would be helpful.
- Second point in the challenges section. I see what you are saying here – but might need a little rewording. If you send it to someone who works on CM connections and say you want to resurrect the field they are working in, some people may take this the wrong way (I say this from experience,  having said similar things to people working in vestibular labs about how the field seemed to have gone cold, and it was often misinterpreted!)
- I agree the EMG is going to be an issue. I should probably read a bit more about surface EMG in humans as I really have no idea what people usually do in these tasks. Do people ever do combinations of fine wire and surface in the same subject? If you had one or two “ground truth” muscles in a recording, would that help validate/parse the signal from the surface electrode?

## Philip
- fine/flexible manipulation of objects is one of the big feats of human CNS evolution
- asking what are the (adaptive) constraints on a system is a wise question to ask.
- I don't get how you disentangle role of cortical from subcortical/spinal stuff in this study (other than by relating them to fractions and syns, which assumes the hypothesis is correct). Is that a major goal though?
- Would be good to see a specific task just as an example. Maybe even with a figure.
- What are a couple possible strategies for solving this task? Is the experiment you propose able to distinguish them? Even better, would the experiment also be able to demonstrate the existence of a third, unexpected strategy that could give you insight into control systems?
- "As far as we know, there is no prior work characterizing the difference between learning novel sensorimotor mappings which include perturbative elements." I feel like sensorimotor mapping and perturbations are psychophysics' bread and butter, respectively, so there must be some.
- Brief comments on prior tasks are unclear and depend on having already read those papers.
- 2nd to last sentence says "using direct electromyographic control" -- was this part of the plan the whole time, or just bringing it up at the end for fun? Would need more convincing for DEC.

## Kelly
- old/new M1: what method? What cortical layer? Know the details!
- Huk paper: what analysis? What statistical result?
- What is the key figure, abstract, summary of the ideal paper? the ideal result?
- Measure proxies for other things? EKG? Pupil? Skin conductance?
- Make intuitive, interesting visuals (a la Huk)
- What are our inbuilt priors? How do they help us learn?
- wisdom:
	- Measuring “learning” is difficult-- subject to subject variation is very high
	- The hand, even with pure EMG control, will have inbuilt, evolutionary constraints
	- Once you have the class of experiment-- take one specific case and run with it

## Nathan (25/7/19)
operational definitions of myocontrol and neurocontrol
this project provides a testable definition of myo- and neurocontrol
one mapping to start with:
- two motor units that are on the exact same muscle
- any sort of submuscular control that can be validated
Once you present a well thought through experiment, then we can offer specific feedback.

## After doing Tim’s task:
- We’re building an internal model of the task structure, and we might even have competing models to drive decisions
- How much data do we use from the past to alter our current model(s)?
- We might take inspiration from “active learning” or “online learning” or “incremental learning” which uses streaming data to alter models. How does that evolving model then inform actions/policy?
- Data Horizon:  How quickly do you need the most recent datapoint to become part of your model?  Does the next point need to modify the model immediately, or is this a case where the model needs to behave conditionally based on that point?  If it is the latter, perhaps this is a time-series prediction problem rather than an incremental learning problem.
- Data Obsolescence:  How long does it take before data should become irrelevant to the model?  Is the relevancy somehow complex?  Are some older instances more relevant than some newer instances?  Is it variable depending on the current state of the data?  Good examples come from economics; generally, newer data instances are more relevant.  However, in some cases data from the same month or quarter from the previous year are more relevant than the previous month or quarter of the current year.  Similarly, if it is a recession, data from previous recessions may be more relevant than newer data from a different part of the economic cycle.
- Generalization of task structure (apply acquired models to solve similar, but noticeably different, task) -- or maybe new sensory feedback? This feels like structural learning

## Implications / Future / Wide Angle
- The promise of a noninvasive neural interface may seem like science fiction, but many groups are making headway in this direction, highlighting the large amount of information present in a noisy surface EMG signal.
- For any neural interface, there exists a learning gap between the output and the intended sensory feedback. This gap can be filled if an appropriate model is constructed such that input and output match in a predictable manner.
- For such an interface to accord properly with our intentions, we need to better characterize the “learnability” constraints of such models. By characterizing these constraints and modeling the strategies used to acquire internal models of new sensorimotor mappings, we can better understand how to develop interfaces that accord with our natural ability and thus move closer to the best interface—one that you forget is there.
- I want to find out what constraints exists in motor learning, and how this relates to human-machine interfaces. That is, what constraints must we consider when designing interactions with machines? What sorts of principles can we use to facilitate such interactions in order to best extend our minds into the machine?
- What are the limits of what we can learn? How can we quantify learnability?
- Does the brain/body use a compressed sensing strategy in the face of uncertainty?
What do you do if you’re in an unlearnable environment?
How can we quantify learnability (apart from the biomechanical constraints) and how does this tell us something about cognition, learning— our strategies for learning?

## Andy
Try and tighten up the first page (more specifics on this below), this may seem arbitrary but it helps to have all your main points up front.
I wonder if there is a way you can pull the three bullet point aims on the first page into one overall question..? It seems a little to broad at the moment. What if you outlined the aim as to “connect work on muscle synergies, corticomotoneuronal connections and algorithms of motor control to explore the limitations of human motor output and learning and develop mechanistic models”. Maybe this is still a bit clunky, but I’m looking for something that brings it closer to one question, even if the question is vague at this stage.
I would remove the list of parameters on the first page, potentially move it to the end where it could fit in the “challenges” section?
The dimensionality description is good
The list of questions at the top of page two I think is again a bit too much. Try and limit this down to 2-3 of the questions you think we can really make headway on.
The part about CM connections and online error corrections is a great thought. Is there much on this?
“..the purpose of CM connections is dealing with online error corrections”. “Purpose” seems to be leading the section in the direction of saying that CM connections exist to help deal with the perturbations..is this what you’re thinking? Perhaps a similar point is that synergies may be set up to reduce the computational power required to generate specific common movements, but this comes at a cost of online corrections. So, how does the nervous system deal with this?
The Prior Relevant tasks section does require some knowledge of each study to make the best use of your points. A line stating what each study looked at/their task design would be helpful.
Second point in the challenges section. I see what you are saying here – but might need a little rewording. If you send it to someone who works on CM connections and say you want to resurrect the field they are working in, some people may take this the wrong way (I say this from experience,  having said similar things to people working in vestibular labs about how the field seemed to have gone cold, and it was often misinterpreted!)
I agree the EMG is going to be an issue. I should probably read a bit more about surface EMG in humans as I really have no idea what people usually do in these tasks. Do people ever do combinations of fine wire and surface in the same subject? If you had one or two “ground truth” muscles in a recording, would that help validate/parse the signal from the surface electrode?
Philip
1) fine/flexible manipulation of objects is one of the big feets of human CNS evol
2) asking what are the (adaptive) constraints on a system is a wise question to ask.
I don't get how you disentangle role of cortical from subcortical/spinal stuff in this study (other than by relating them to fractions and syns, which assumes the hypothesis is correct). Is that a major goal though?
Would be good to see a specific task just as an example. Maybe even with a figure.
What are a couple possible strategies for solving this task? Is the experiment you propose able to distinguish them? Even better, would the experiment also be able to demonstrate the existence of a third, unexpected strategy that could give you insight into control systems?
"As far as we know, there is no prior work characterizing the difference between learning novel sensorimotor mappings which include perturbative elements." I feel like sensorimotor mapping and perturbations are psychophysics' bread and butter, respectively, so there must be some.
Brief comments on prior tasks are unclear and depend on having already read those papers.
2nd to last sentence says "using direct electromyographic control" -- was this part of the plan the whole time, or just bringing it up at the end for fun? Would need more convincing for DEC.

## Kelly
old/new M1: what method? What cortical layer? Know the details!
Huk paper: what analysis? What statistical result?
What is the key figure, abstract, summary of the paper?
Measuring “learning” is difficult-- subject to subject variation is very high
Measure proxies for other things? EKG? Pupil? Skin conductance?
Make intuitive, interesting visuals (a la Huk)
The hand, even with pure EMG control, will have inbuilt, evolutionary constraints
What are these? How do they help us learn?
Once you have the class of experiment-- take one specific case and run with it
Notes

## After doing Tim’s task:
We’re building a model of the task structure, and we might even have competing models to drive decisions
The amount of data we use from the past to alter our current model(s)
We might take inspiration from “active learning” or “online learning” or “incremental learning” which uses streaming data to alter models. How does that evolving model then inform actions/policy?
Data Horizon:  How quickly do you need the most recent datapoint to become part of your model?  Does the next point need to modify the model immediately, or is this a case where the model needs to behave conditionally based on that point?  If it is the latter, perhaps this is a time-series prediction problem rather than an incremental learning problem.
Data Obsolescence:  How long does it take before data should become irrelevant to the model?  Is the relevancy somehow complex?  Are some older instances more relevant than some newer instances?  Is it variable depending on the current state of the data?  Good examples come from economics; generally, newer data instances are more relevant.  However, in some cases data from the same month or quarter from the previous year are more relevant than the previous month or quarter of the current year.  Similarly, if it is a recession, data from previous recessions may be more relevant than newer data from a different part of the economic cycle.
Generalization of task structure (apply acquired models to solve similar, but noticeably different, task) -- or maybe new sensory feedback?

The promise of a noninvasive neural interface may seem like science fiction, but many groups are making headway in this direction, highlighting the large amount of information present in a noisy surface EMG signal.

For any neural interface, there exists a learning gap between the output and the intended sensory feedback. This gap can be filled if an appropriate model is constructed such that input and output match in a predictable manner.

For such an interface to accord properly with our intentions, we need to better characterize the “learnability” constraints of such models. By characterizing these constraints and modeling the strategies used to acquire internal models of new sensorimotor mappings, we can better understand how to develop interfaces that accord with our natural ability and thus move closer to the best interface—one that you forget is there.

Physiological underpinnings
Modeling prior work
Task setup / data shape

## Active Sensing
Hierarchical Bayesian models -- what does this actually look like…?
Information theoretic constraints -- how are these formalized? (maybe see Braun’s work)
Could this lead to characterizing some information theoretic constraints on how we can learn new skills? How we use strategies to cope with this limitations?

What internal models cannot be learned?

What strategies are used for learning, and how do they relate to the statistical structure of the task?
Can we engineer “latent” structure in a sensorimotor mapping to characterize the constraints of a neural learning system?

For a large number (trials) of a random system/mapping with a set of parameters, we can compare the statistics of the learning process for the subject and an online algorithm. The algorithm can serve as a model, and the statistics as a confirmatory hypothesis analysis.

Adversarial Mappings
Sensorimotor mappings that are unlearnable
Probabilistic
Uncertainty
Can we engineering mappings with temporal correlations? What are the limits of such an internal model of this dynamics?
Is the mapping a dynamical system? What aspect of dynamical systems can we (not) represent and use in the brain?
You are the plant, like a sensorimotor mapping
You are the controller, you have to understand the outcomes of your control inputs
What is the difference between these two versions?
Questions
How do we generate these structured mappings?

Story
I want to find out what constraints exists in motor learning, and how this relates to human-machine interfaces. That is, what constraints must we consider when designing interactions with machines? What sorts of principles can we use to facilitate such interactions in order to best extend our minds into the machine?

Nitty Gritty
Linear (one to one) map between target position and finger force
Linear (one to one) map between “force” (delta) and finger force
Autoregressive (?), time correlations

## Task
Like this:
Lawful tracking of visual motion in humans, macaques, and marmosets in a naturalistic, continuous, and untrained behavioral context
Eye movements of Humans, macaques, marmosets are recorded while watching a random walker visual stimulus. A prediction is made based on a Kalman filter approach.
How can we extend this type of task to a motor regime?
But how does this become a motor task? How do we define the parameters of learning the mapping?

Spatial (State-dependent) correlation structure
Temporal correlations
Goal: understand how you actively discover internal/probabilistic models, your sampling strategies in a novel environment
Continuous
Knobs
Sensory statistics of the scene
Sensorimotor mapping / Control inputs
Not dependent on limb mechanics
Focused on muscles of the hand (for CM connections)
Goal-driven but intuitive (preferably without explanation
Think about priors? E.g. remaining upright…
Ethological
Complex / Naturalistic / High-dimensional
Perhaps it is generative based on state? So no two subjects experience the exact same environment
Why hand muscles directly?
This removes the transformation from brain to hand coordinates, we’re directly tapped into the muscle space to test the limits of what can be learned by direct motor output

Questions
What approximations do we make when we’re developing internal models?
What strategies do we use to explore a high-dimensional state space?
Active sensing?
What are the limits of what we can learn? How can we quantify learnability?

Does the brain/body use a compressed sensing strategy in the face of uncertainty? What do you do if you’re in an unlearnable environment?
How can we quantify learnability (apart from the biomechanical constraints) and how does this tell us something about cognition, learning— our strategies for learning?

Thinking about the hands in particular, which seem to have far fewer constraints computationally / behaviorally as the arm, how can we begin to connect motor learning control to a broader understanding of learning and control in general?
What do we mean when we say learning and control in the context of the hands, who seem to have more “freedom” than the other limbs.
That is, the hands can be utilized as an output of cognition over the arms, which are more constrained.

Model
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
This hierarchy relies on the statistics of the environment in which learning is taking place
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

Obviously the statistics of the task space drive the representation of movement, but how do we utilize (or sample?) the statistics of the environment to efficiently produce movements that achieve task goals?

The reverse engineering problem is cool-- we present the system with a problem to solve, and we keep giving it problems until we define the boundaries of what it can learn, not learn, learn well, learn not-so-well. We have to construct these tasks in such a way that they tell us something specific.

What makes a mapping learnable, and how does a system change to learn a new mapping? What has evolution done to accommodate mappings while retaining (or evolving) flexibility / dexterity?
How does robotics try to deal with this?
The system is hierarchical-- it has overlapping motor pools, synergies, reflexes, direct cortical overriding signals. It seems that it has a higher amount of direct control the further distal you go in the human arm.
The dynamics of the types of tasks humans can learn to do our crazy-- so we have to give up modeling them and learn how the system adapts to produce these outputs without an explicit model-- where does the “model” live?
What types of internal models can you learn? Not learn?
The motor system seems to effectively solve difficult inverse problems-- how

Drill in on the types of mappings, classes of mappings, that are learnable-- this tells us something about how the brain is undergoing the learning/adaptation process. This is the learning question, and it gives us insight into a model for how the brain learns to adjust for error in it’s task. We can even study this simply with a force output to start.
The second question is what the muscles are doing during the learning problem, and tying this back to our knowledge of the physiology of the system. The problem here is not providing mere speculation on what’s happening under the hood, but generating testable hypotheses. This step also required being very careful about the data collection process in order to make sure we have data that is capable of supporting out hypotheses
The next step is to design perturbations, within the task and for the mapping, and detect, for a given mapping, whether synergies are re-recruited or if other mechanisms are used to accommodate for unpredictable perturbations.

Interesting that users found it frustrating to adjust the mapping after each trial block-- how can we continually shift the mapping to maintain constant learning, or show some metalearning?

title: Learning and relearning in virtual motor control tasks
Perhaps with nonlinear mappings there is no closed form control solution, but we are able to control the system with our bodies. Is understanding how the system is solved (quickly?) by biological neural control connected to how it might be solved using, say, a neural network?
Nathan (25/7/19)
operational definitions of myocontrol and neurocontrol
this project provides a testable definition of myo- and neurocontrol
one mapping to start with:
- two motor units that are on the exact same muscle
- any sort of submuscular control that can be validated
Once you present a well thought through experiment, then we can offer specific feedback.
Meta
Strategies for admin meetings
leverage the continuation aspect of the work
Show that i know where
Show that i’m going building on a foundation
bring slides!!!!
project goal
prior art
outline / plan
lingering questions (who is my advisor?)
what is the specific question/experiment?
First stage
Learn fixed mapping between some control outputs and some environmental parameters
Second stage
Perturbing that mapping appropriately based on the question of interest
Andy 17/7/19
Think muscle → output → (feedback), less about the game itself
Literature on activating single muscles in the hand/forearm? Single digit control?
Send todorov finger, remapping papers
Are synergies learned or developed or both?
Two questions
Learning / unlearning of synergies? Mappings?
Perturbations to learned mappings
Goal
Design a game that provides the right feedback to tease apart our hypothetical spinal and supraspinal controllers-- make a claim that there are both synergies and not synergies-- perhaps voluntary control overrides these synergies, and once they are learned (the modules are combined in a sequence or on a manifold) they form a new module / synergy. That is, synergies are neither learned nor set in development, they are two facets of the same system. They appear as a result of the brain’s solution to the redundant control problem at any given time.
Design a task that recruits synergies, breaks synergies apart, and reforms synergies. Show that a controller that generates this behavior is a hierarchical one that leverages these modules for combination, recombination, consolidation to learn new motor skills and adapt skills to new inputs and environments.
Athena (23/7/19)
What is the goal?
What is the limitation of control?
Wire up a bunch of EMG, build a motor map?
See how this map changes with an “unnatural” task
How do you create EMG → feedback mappings in a principled manner?
Could spend a whole PhD assaying tasks, mappings to uncover what is “intuitive” and what isn’t…
We know this for synergies, but do we know it for non-biomechanically constrained movements?

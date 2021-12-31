As we've touched on many times in this series, computers are incredible at storing, organizing, fetching, and processing huge volumes of data. That's perfect for things like e-commerce websites with millions of items for sale and for storing billions of health records for quick access by doctors.

But what if we want to use computers not just to fetch and display data, but to actually make decisions about data? This is the essence of machine learning, algorithms that give computers the ability to learn from data, and then make predictions and decisions.

Computer programs with this ability are extremely useful in answering questions like 'is this email spam?', 'does a person's heart have arrhythmia?', or 'what video should YouTube recommend after this one?'.

While useful, we probably wouldn't describe these programs as intelligent in the same way we think of human intelligence. So even though the terms are often interchanged, most computer scientists would say that machine learning is a set of techniques that sits inside the even more ambitious goal of artificial intelligence or AI for short.

Machine learning and AI algorithms tend to be pretty sophisticated. So rather than wading into the mechanisms of how they work, we're going to focus on what the algorithms do conceptually.

Let's start with a simple example: deciding if a moth is a luna moth or an emperor moth. This decision process is called classification and an algorithm that does it is called a classifier.

Although there are techniques that can use raw data for training like photos and sounds, many algorithms reduce the complexity of real-world objects and phenomena into what are called features. Features are values that usefully characterize the things we wish to classify.

For our moth example, we're going to use two features: wing span and mass. In order to train our machine learning classifier to make good predictions, we're going to need training data. To get that, we'd send an entomologist out into a forest to collect data for both luna and emperor moths.

These experts can recognize different moths. So they not only record the feature values, but also label that data with the actual moth species. This is called labeled data.

Because we only have two features, it's easy to visualize this data in a scatter plot. Here, I've plotted data for 100 emperor moths in red an 100 luna moths in blue. We can see that the species make two groupings, but there's some overlap in the middle.

So it's not entirely obvious how to best separate the two. That's what machine learning algorithms do: find optimal separations. 

I'm just going to eyeball it and say that anything less than 45mm in wingspan is likely to be an emperor moth. We can add another division that says additionally, mass must be less than 0.75 in order for our guess to be emperor moth.

These lines that chop up the decision space are called decision boundaries. If we look closely at our data, we can see that 86 emperor moths would correctly end up in the emperor decision region, but 14 would end up incorrectly in luna moth territory. On the other hand, 82 luna moths would be correct, with 18 falling onto the wrong side.

A table like this, showing where a classifier gets things right or wrong, is called a confusion matrix. Which probably should have also been the title of the last two movies in the Matrix trilogy.

Notice that there's no way for us to draw the lines that give us 100% accuracy. If we lower our wingspan decision boundary, we misclassify more emperor moths as lunas. If we raise it, we misclassify more luna moths. 

The job of machine learning algorithms at a high level is to maximize correct classifications while minimizing errors. On our training data, we get 168 moths correct and 32 moths wrong. For an average classification accuracy of 84%.

Now using these decision boundaries, if we go out into teh forest and encounter an unknown moth, we can measure its features and plot it onto our decision space. This is unlabeled data. Our decision boundaries offer a guess as to what species the moth is. In this case, we'd predict it's a luna moth.

This simple approach of dividing the decision space up into boxes can be represented by what's called a decision tree, which would look like this pictorially or can be written in code using IF statements like this.

A machine learning algorithm that produces decision trees needs to choose what features to divide on. And then for each of those features, what values to use for the division. 

Decision trees are just one basic example of a machine learning technique. There are hundreds of algorithms in computer science literature today and more are being published all the time. A few algorithms even use many decision trees working together to make a prediction.

Computer scientists smugly call those forests, because they contain a lot of trees. There are also non-tree-based approaches like support vector machines, which essentially slice up the decision space using arbitrary lines.

And these don't have to be straight lines. They can be polynomials or some other fancy mathematical function. Like before, it's the machine learning algorithm's job to figure out the best lines to provide the most accurate decision boundaries.

So far, my examples have only had two features, which is easy enough for a human to figure out. If we had a third feature, let's say length of antennae, then our 2D lines become 3D planes, creating decision boundaries in three dimensions. 

These planes don't have to be straight either. Plus a truly useful classifier would contend with many different moth species. Now I think you'd agree, it's getting too complicated to figure out by hand, but even this is a very basic example: just three features and five moth species. We can still show it in this 3D scatter plot.

Unfortunately, there's no good way to visualize four features at once, or twenty features, let alone hundreds or even thousands of features. But that's what many real-world machine learning problems face. 

Can you imagine trying to figure out the equation for a hyperplane rippling through a thousand-dimensional decision space? Probably not, but computers with clever machine learning algorithms can. And they do, all day long, on computers at places like Google, Facebook, Microsoft, and Amazon.

Techniques like decision trees and support vector machines are strongly rooted in the field of statistics. Which has dealt with making confident decisions using data long before computers ever existed. There's a very large class of widely used statistical machine learning techniques.

But there are also some approaches with no origins in statistics. Most notable are artificial neural networks, which were inspired by neurons in our brains. For a primer of biological neurons, check out our 3-part overview here.

But basically, neurons are cells that process and transmit messages using electrical and chemical signals. They take one or more inputs from other cells, process those signals, and then emit their own signal. These form huge, interconnected networks that are able to process complex information, just like your brain watching this YouTube video.

Artificial neurons are very similar. Each takes a series of inputs, combines them, and emits a signal. Rather than being electrical or chemical signals, artificial neurons take numbers in and spit numbers out. They are organized into layers that are connected by links, forming a network of neurons, hence the name.

Let's return to our moth example to see how neural nets can be used for classification. Our first layer, the input layer, provides data from a single moth needing classification. Again, we'll use mass and wingspan.

At the other end, we have an output layer with two neurons, one for emperor moth and another for luna moth. The most excited neuron will be our classification decision. In between, we have a hidden layer that transforms our inputs into outputs and does the hard work of classification.

To see how this is done, let's zoom in to one neuron in the hidden layer. The first thing a neuron does is multiply each of its inputs by a specific weight. Let's say 2.8 for the first input and 0.1 for its second input. Then it sums these weighted inputs together, which in this case is a grand total of 9.74.

The neuron then applies a bias to this result. In other words, it adds or subtracts a fixed value. For example, -6.0 for a new value of 3.74.

These bias and inputs weights are initially set to random values when a neural network is created. Then an algorithm goes in and starts tweaking all those values to train the neural network, using labeled data for training and testing.

This happens over many interactions, gradually improving accuracy. A process very much like human learning. 

Finally, neurons have an activation function, also called a transfer function that gets applied to the output, performing a final mathematical modification to the result.

For example, limiting the value from a range from -1 and 1, or setting any negative values to 0. We'll use a linear transfer function that passes the value through unchanged. So 3.74 stays as 3.74.

So, for our example neuron, given the inputs 0.55 and 82, the output would be 3.74. This is just one neuron, but this process of weighting, summing, biasing, and applying an activation function is computed for all neurons in a layer. And the values propagate forward in the network one layer at a time.

In this example, the output neuron with the highest value is our decision: luna moth. Importantly, the hidden layer doesn't have to be just one layer. It can be many layers deep. This is where the term Deep Learning comes from. 

Training these more complicated networks takes a lot more computation and data. Despite the fact that neural networks were invented over 50 years ago, deep neural nets have only been practical very recently thanks to powerful processes, but even more so wicked-fast GPUs.

So thank you gamers, for being so demanding about silky-smooth frame rates.

A couple of years ago, Google and Facebook demonstrated deep neural nets that could find faces in photos as well as humans. And humans are really good at this. It was a huge milestone! Now deep neural nets are driving cars, translating human speech, diagnosing medical conditions, and much more.

These algorithms are very sophisticated, but it's less clear if they should be described as intelligent. They can really only do one thing. Like classify moths, find faces, or translate languages.

This type of AI is called weak AI or narrow AI. It's only intelligent at specific tasks. But that doesn't mean it's not useful. I mean, medical devices that can make diagnoses and cars that can drive themselves are amazing.

But do we need those computers to compose music and look up delicious recipes in their free time? Probably not. Although, that would be kind of cool.

Truly general purpose AI, one as smart and well-rounded as human, is called strong AI. No one has demonstrated anything close to human level artificial intelligence yet.

Some argue it's impossible, but many people point to the exposure of digitized knowledge like Wikipedia articles, webpages, and YouTube videos as the perfect kindling for strong AI.

Although you can only watch a maximum of 24 hours of YouTube a day, a computer can watch millions of hours. For example, IBM's Watson can consults and synthesizes information from 200 million pages of content, including the full text of Wikipedia.

While not a strong AI, Watson is pretty smart and it crushed its human competition in Jeopardy way back in 2011. Not only can AIs gobble up huge volumes of information, they can also learn over time. Often much faster than humans.

In 2016, Google debuted AlphaGo, a narrow AI that plays the fiendishly complicated board game: Go. One of the ways it got so good and able to beat the very best human players, was by playing clones of itself millions and millions of times.

It learned what worked and what didn't and along the way discovered successful strategies all by itself. This is called reinforcement learning and it's a super powerful approach. In fact, it's very similar to how humans learn.

People don't just magically acquire the ability to walk. It takes thousands of hours of trial and error to figure it out. Computers are now on the cusp of learning by trial and error. And for many narrow problems, reinforcement learning is already widely used.

What will be interesting to see is if these types of learning techniques cna be applied more broadly to create human like strong AIs that learn much like how kids learn, but at super accelerated rates.

If that happens, there are some pretty big changes in store for humanity. A topic we'll revisit later. 

<br>

컴퓨터가 어떻게 등장하게 되었는지, 어떤 원리로 동작하는지에 대해 공부했습니다.

- 수학적, 통계적인 부분에서 인간의 능력은 한계에 부딪혔고, 이를 기계적으로 해결하려는 시도와 함께 컴퓨터의 근간이 되는 여러 장치가 개발됨
- 컴퓨터는 내부의 회로에 전기가 흐르는지 여부를 이진수로 취급하며, 여러 논리 회로를 조합하여 이러한 전기 신호를 조작하는 방식으로 동작함
- 컴퓨터의 기초가 되는 구성 요소는 수치적인 계산과 논리 연산을 처리하는 산술 논리 장치와 전기가 흐르는 상태(비트 정보) 를 저장하는 래치임

프로그래밍의 유래와 역사, 프로그래밍 언어가 발전해온 과정에 대해 공부했습니다.

- 기계어는 명령 코드와 기억 장치 주소로 구성되는 명령어이며, 논리 회로로 구성된 컴퓨터가 직접적으로 받아들일 수 있는 이진수 정보로 구성됨
- 기계어는 인간이 읽고 쓰기에는 적합하지 않아서, 프로그램을 설계할 때는 의사 코드를 사용하고, 그것을 다시 기계어로 번역하는 식으로 활용됐음
- 이러한 번거로운 작업에 지친 프로그래머들은, 이진수 명령 코드마다 해당 코드의 내용을 쉽게 떠올릴 수 있게 도와주는 니모닉 문자를 지정했음
- 그리고, 이러한 니모닉을 프로그램 작성에 직접 활용할 수 있도록 하기 위해 개발된 것이 어셈블러이며, 니모닉은 이후, 어셈블리어라고 불리게 됨
- 어셈블리어는 기계어에 1대1로 대응되기 때문에 어셈블러가 하드웨어에 종속될 수밖에 없고, 메모리 주소를 직접 지정해야 한다는 단점이 있음
- 이러한 한계들을 극복하기 위해, 프로그래머들은 프로그래밍 언어와 이러한 프로그래밍 언어를 기계어로 직접 번역하는 컴파일러를 개발하게 됨

<br>

올해 7월에 참가했던 'GDG 썸머 해커톤 w/디프만' 이라는 행사에서, 서버 개발 작업을 진행하며 겪은 일화입니다.

- 저희 팀은 개발자, 디자이너, 기획자가 사이드 프로젝트를 진행할 팀원을 모집할 수 있는 간단한 서비스를 만들고자 했습니다.
- 물론, 기본적인 서버 프로그램을 개발해본 적은 있었지만, 실시간으로 정보를 주고받는 채팅 기능은 만들어본 적이 없었습니다.
- 그래서, 사용 중이던 프레임워크로 채팅 기능을 만드는 법에 대해 찾아봤고, 유튜브에 있는 튜토리얼 영상을 보며 공부했습니다.
- 예제 코드를 보고, 각 변수의 역할과 동작 방식을 파악했고, 코드를 수정하면서, 원래 구현하려던 데로 조금씩 바꿔나갔습니다.
- 하지만 아쉽게도, 배포 환경에서는 채팅 기능이 제대로 동작하지 않았고, 밤을 새워 문제점을 찾아봤지만, 결국 찾지 못했습니다.
- 서버 프로그램은 잘 동작하나, 브라우저에서 웹 소켓이 연결되지 않아 문제였는데, 제대로 해결하지 못해, 아직도 많이 분합니다.
- 백엔드 팀원분을 설득해서 일정과 역할을 조율하고, AWS 설정을 더 건드려봤다면 문제를 해결할 수 있었을 것 같아 아쉽습니다.
- 프론트엔드 팀원분도 일정을 맞추지 못해, 미완성인 채로 마무리되었는데, 제가 나서서 도와줬으면 어땠을까 하는 생각도 듭니다.

<br>

다른 사람과 협업하여 참여했던 프로젝트 중 기억에 남는 프로젝트가 있다면 어떤 것이고 어떤 역할로 어떻게 기여하셨나요?

'GDG 썸머 해커톤 w/디프만' 이라는 행사 때 참여한 프로젝트가 기억에 남네요.
처음 보는 분들과 팀을 이뤄서 주제를 정하고, 기한 내에 서비스를 만드는 프로젝트였어요.
팀 구성은 디자이너 1명, 프론트엔드 1명, 백엔드 2명이었고, 제 역할은 백엔드 개발이었어요.
주제는 사이드 프로젝트가 하고 싶은 사람들이 모일 수 있는 플랫폼을 개발하는 것이었구요.

사이드 프로젝트를 진행하고 싶어도, 같이 할 사람을 구하기가 어렵잖아요?
원하는 데로 인원을 구성하기도, 서로 성향이 잘 맞는지 알아보기도 힘들구요..
그래서 저희는, 사용자들이 직접 방을 만들거나, 방에 참여할 수 있는 서비스를 만들기로 했어요.

저는 방 생성 및 수정, 랜덤 매칭, 실시간 채팅 기능 개발을 담당했어요.
Django라는 프레임워크로 작업을 했고, 기능별로 필요한 동작을 수행하는 API를 개발했죠.
Channels라는 라이브러리를 활용해, 웹 소켓을 활용하는 비동기적 채팅 기능도 구현했어요.

<br>

이런건 AI 가 해결할 수 있지 않을까? 라는 상상을 해보셨나요? 어떤 상상이었나요?

전 직장 다닐 때, 회사 근처 역 입구에 약국이 하나 있었는데, 퇴근하다가 뜬금없이 떠오른 생각이 있어요.
조금 뜬금없는 생각이긴 한데, 약국에서 약을 처방해주는 행위를 기계가 대신 할 수 있지 않을까? 하는 생각이었죠.

의사마다 처방전 필체가 달라서 정확성이 떨어질 수도 있지만, 학습시킬 정보가 충분하면 극복할 수 있을 것 같아요.
물론, 약사분들의 일자리를 침범할 수도 있어서 결과적으로 좋지 않을 수 있지만, 활용될 여지는 충분하다고 생각해요.

그리고, 최근에 친구랑 강릉에 다녀오는 길에, 차 사고가 날 뻔했는데, 그때도 떠오른 생각이 있어요.
자동차 파손 부위를 카메라에 비추거나, 사진을 찍으면 파손율을 계산해주는 AI도 있으면 좋겠다는 생각이에요.

당시, 차가 실제로 긁히거나 하진 않았는데, 파손 여부 확인을 도와줄 뭔가가 있으면 좋겠다고 생각했어요.
실제로 사고가 난 경우에도, 인명 피해는 거의 없는 상황에서 피해 보상을 논의할 때 객관적인 지표를 줄 수 있을 거예요.

<br>

최근에 겪은 문제가 있었나요? 그렇다면 그 문제를 어떻게 해결했나요? (사소하거나, 개인적인 것도 상관 없습니다.)

얼마 전에 어떤 스타트업에서 제안이 와서, 혼자서 과제 프로젝트를 진행했어요.

기능 구현과 문서화, 테스트 코드 작성까지 진행하길 요구했는데, 3일의 기한은 조금 빠듯하다고 생각했어요.
그래서, 기능 구현과 문서화를 우선적으로 마무리하고, 테스트 코드는 시간이 남는다면 진행하기로 정했죠.
우선, 어떤 기능부터 구현할지 순서를 정했고, 그 후, 순서대로 하나씩 구현해서, 문서화까지는 마무리할 수 있었어요.

하지만, 테스트 코드는 회원가입 부분만 작성하고, 주석도 아예 못 남겨서, 완성도 면에서는 많이 부족했던 것 같아요.
기능을 다 구현하는 것보다, 일부라도 테스트 코드까지 완벽히 구현하는 것이 더 좋았을까 하는 생각도 드네요..

결국 떨어지긴 했지만, 세워둔 계획대로 프로젝트를 진행하고, 문서 작성을 연습할 기회가 생겨서 좋았어요.

<br>

프로그래밍 외에 다른 다룰 수 있는 툴 혹은 직무 경험이 있으신가요? 있으시다면 어떤 경험을 하셨는지 알려주세요. 없으시다면 프로그래밍 외에 가지고 계신 관심사, 취미에 대해 이야기 해주셔도 좋습니다.

컴퓨터 관련 분야로 전향하기 전에, 다른 직장에서 일했던 경험이 있어서, 웬만한 건 눈치껏 배워서 할 수 있어요.
정말 전문적인 지식이 필요한 도구라면, 어느 정도 익숙해지기까지 시간이 좀 필요하긴 하지만, 큰 문제는 없어요.

프로그래밍 외에는 음악에 관심이 많은데, 장르 상관없이, 듣는 거 부르는 거 모두 좋아해요.
국내 가요, 외국 가요(팝송), 일렉트로닉(EDM), 클래식 기타 연주 등등, 가리지 않고 듣는 편이에요.
개인적으로 좋아하는 곡은 Myself, Piano Man, Good Grief, 한숨, 가짜 탱고 등이 있어요.

다양한 소리를 통해 감정을 공유하고, 생각을 표현할 수 있다는 것이 매력적이라고 생각해요.
그렇게 잘 부르는 편은 아니지만, 노래를 부르면 기분이 상쾌해지고, 스트레스도 잘 풀려서 좋더라구요.

<br>

마지막 질문이에요! 최호준님. 카카오 브레인 PathFinder 활동으로 어떤 부분을 기대하시나요?

인공지능 모델을 실제 상용 서비스에 적용하는 프로젝트를 직접 경험해볼 수 있다는 게 엄청나게 기대돼요.
어떤 문제를 다루게 될지, 또, 그걸 어떻게 해결할지 고민하면서 많은 걸 배울 수 있을 것 같기도 하구요.

개인적으로, 데이터 엔지니어 직무에 관심이 있는데, 관련 종사자분들도 뵐 수 있을 것 같아서 기대돼요.
또, 카카오 인프라를 활용하면서, 빅테크 기업의 여러 체계를 경험해볼 수 있다는 것도 큰 매력인 것 같아요.

<br>

모각코 (모여서 각자 코딩)
Gdg Campus Korea
14일 devfest university 기간동안 매일매일 진행되는 모.각.코! 같이 코딩도하고 타대학 학생과 현업개발자들과의 네트워킹 기회까지 얻어봐요. 12회 이상 참여 시 DevFest 2021 티셔츠👕 & 스티커 🔵증정 Full 참여 시 Extra Gift! (아직은 찌끄릿-) 까지 다양한 혜택이 있습니다~!

10-3000:00~00:00
출석

개발자의 취업과 진로 - 카카오, 토스 개발자
성신여자대학교
현직 카카오, 토스 개발자의 취업 이야기와 백엔드, 프론트엔드의 진로에 대한 소개와 질의응답 시간을 가집니다!

10-3118:00~19:00
출석

효율적인 문제 해결 with 알고리즘
연세대학교 미래캠퍼스
알고리즘의 의미와 알고리즘의 평가 방법(복잡도)에 대해서 소개하고, 코딩테스트와 대회의 차이점, 알고리즘 공부 방법, 온라인 저지, 사용해야 하는 프로그래밍 언어 등 이 분야를 접해본 적 없는 초심자가 궁금할법한, PS에 대한 다양한 주제를 간략하게 다룹니다.

10-3119:20~19:50
출석

강화학습으로 만든 테트리스AI
연세대학교 미래캠퍼스
강화학습은 환경과 상호작용하며 시행착오를 통해 보상을 최대화하는 행동은 더 자주 선택하도록 하는 학습 방법입니다. 강화학습의 기본 개념에 대해 살펴본 뒤에, 테트리스 게임에 적용하여 실제 게임에서 환경을 구현하고 강화학습의 핵심 개념들을 적용하는 과정을 소개합니다.

10-3120:00~20:40
출석

다양한 Gan - 경찰과 도둑
연세대학교 미래캠퍼스
Gan에 대해 간단하게 설명하고, 다양한 Gan(ex. Style Gan, Cycle Gan, Sin Gan 등)과 GitHub의 흥미로운 모델을 소개합니다. 각 모델이 어떤 과정을 통하여 학습이 이루어지고 다른 모델과의 차이점은 무엇이며 이를 이용하였을 시에 얻는 이점에 대해 발표합니다.

10-3120:50~21:30
출석

자연어 입문 - 네이버 영화리뷰를 활용하여 감성 분석 해보기
연세대학교 미래캠퍼스
한국어 글자 데이터를 전처리하는 방법을 실습하고, 딥러닝 기술로 네이버 영화 리뷰데이터(Naver Sentiment Movie Corpus, NSMC)가 긍정리뷰인지 부정리뷰인지 감성 분석 및 분류하는 실습을 진행합니다.

10-3120:00~21:30
출석

비어 모각코(부제: 후회없는 월요일 알콜코딩🍻)
숙명여자대학교
전체적인 진행은 jukebox.today로 신청곡 받으며 감상하기 + 모각코고, 오후 10시 정각에 운동장 한가운데에서 O/X 퀴즈 진행합니다.

11-0121:00~23:00
출석

음주코딩(飮酒编码) - 강한 자만이 살아남는다!
한국외국어대학교
원하는 음료와 함께 모각코를 하는 시간! 이벤트를 즐기며 가볍게 네트워킹 하는 시간입니다.

11-0220:00~22:00
출석

개발자의 학습법
동의대학교
평소에 다른 사람들은 어떤 식으로 학습을 하는지 물어보고, 어떤 장단점이 있을지, 어떤 방식이 자신에게 적절할지 얘기를 해보는 토크 콘서트!

11-0220:00~21:00
출석

나는 어쩌다 000이 되기로 했나
서울과학기술대학교
"나는 어쩌다... 000이 되기로 했나" 를 주제로 4분의 연사 분들의 이야기를 들어볼까요?

11-0319:00~21:00
출석

시리야 그림 그려줘 - 그림 그리는 인공지능
상명대학교
ml5.js와 sketch RNN을 알아보고, sketch RNN을 직접 실습해봅니다.

11-0419:00~20:40
출석

Android Day
인하대x대진대
3가지 코드랩과 개발 진로 고민상담 부스가 동시에 모두 운영됩니다.

11-0519:00~21:00
출석

코린이부터 코인물까지 함께하는 고민상담!
대진대학교
여러분들의 고민과 사연을 낭독하고 조언하는 본격 고민 상담시간!

11-0519:00~21:00
출석

Git Day
인하대x한양대
Github를 활용한 나만의 프로필 만들고, 포트폴리오 완성하기

11-0619:00~21:00
출석

개처럼 성장해서 정승처럼 개발하기 - 개발자 성장 과정 공유
서울시립대
성장 장인 5분의 패널 분들의 성장 과정기를 공유하고, 네트워킹 하는 시간

11-0719:00~21:00
출석

나만의 Slack - 이모지 제작 및 슬랙봇 제작 가이드
순천향대학교
슬랙 이모지를 직접 제작해보고, 콘테스트가 진행됩니다.

11-0818:00~19:00
출석

Flutter 릴레이 코딩
순천향대학교
Flutter로 릴레이 코딩을 해봅시다!

11-0819:00~21:00
출석

개발 상식 퀴즈대회
부산대
O/X 퀴즈 와 개발과 관련된 퀴즈문제를 풀고 퀴즈왕이 되어보자~

11-0919:00~21:00
출석

DevFest 방탈출
숭실대학교
단서를 찾아 답을 맞춰 다음 스테이지로 넘어가는 방탈출 게임

11-0920:00~22:00
출석

보안과 함께 하는 개발, 시큐어코딩
이화여자대학교
요즘 대세 보안, 하루만에 시큐어코딩 핵심만 배우고 보안 개발자로 거듭나봐요!

11-1019:00~21:00
출석

개발자로서 첫 취업 성공하기 A-Z
삼육대, 한양대
학업과 실무의 괴리 + 학업과 취준 병행하기 취직후 신입 개발자가 해야하는 일 + 여가시간에 하면 좋은 자기계발

11-1117:30~19:30
출석

웹으로 웰하기 살기
인하대학교
Web 개인 프로젝트로 취업 뽀개기

11-1119:30~21:00

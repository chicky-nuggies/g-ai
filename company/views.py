from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import boto3
import json
import regex

brt = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")

def chatbot(user_input):

            # Clean and format user input
            clean_input = user_input.strip().lower()

            final_input = "\n\nHuman: {}\n\nAssistant:".format(clean_input)
            print(clean_input)


            body = json.dumps({
            "prompt": final_input,
            "max_tokens_to_sample": 300,
            "temperature": 0.1,
            "top_p": 0.9,
            })

            modelId = 'anthropic.claude-v2'
            accept = 'application/json'
            contentType = 'application/json'

            response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

            response_body = json.loads(response.get('body').read())

            # text
            response = response_body.get('completion')

            # Prepare generated text for HTML display
            # escaped_text = cgi.escape(response)

            # Render HTML page with generated text
            return response
  
def json2dict(j):
    pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
    return json.loads("".join(pattern.findall(j)))

def ai(ver, prompt):
    # brt = boto3.client(service_name='bedrock-runtime')
    if ver == 1:
        modelId = 'anthropic.claude-v1'
    else:
        modelId = 'anthropic.claude-v2'
        
    accept = 'application/json'
    contentType = 'application/json'

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 3000,
        "temperature": 0.1,
        "top_p": 0.9,
    })

    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())

    # text
    return(json2dict(response_body.get('completion')))

def gen_profile():
    email = '''Subject	Content
Join the Peace Rally for Palestine!	Hi everyone, I'm organizing a peaceful rally in support of Palestine's rights. It's crucial to stand together for justice. Let's make our voices heard. Details enclosed.
Office Charity Drive Proposal	Hi Team, I've outlined a plan for a charity event to aid victims of conflict zones. Let's discuss how we can contribute and make a meaningful impact together.
Islamic Lecture Insights	Salaam everyone, there's an inspiring lecture series at the mosque this weekend. I believe it'll be enlightening for all of us. Let's attend together and grow spiritually.
Concerns Regarding Recent Company Practices	Dear [Company], I'm deeply troubled by recent events and your connection to conflict regions. As a consumer, I feel compelled to boycott your products until these issues are addressed.
Fast Food Favorites!	Hey friends, craving a quick bite? Here are my top picks from local fast-food joints. Trust me, these dishes are a treat!
Collaboration Proposal: Social Awareness Event	Hello [NGO], I admire your work. Let's discuss collaborating on an awareness event to shed light on social issues affecting our community.
Reflections on Faith and Unity	Hi [Friend], today's lecture was profound. It stirred thoughts about the importance of unity and compassion in our lives. I'd love to hear your thoughts.
Sustainability Initiative Proposal	Hi [Manager], I've been contemplating ways we can foster sustainability in our workplace. Let's explore strategies to reduce our environmental footprint.
Sign & Share: Petition for Palestinian Rights	Hi everyone, signing this petition can bring positive change for Palestine. Let's spread the word and stand up for justice together!
Community Action: Boycott Awareness	Dear all, I've compiled a list of brands involved in the conflict. Let's make informed choices and support ethical businesses. Let's chat about this!
Urgent: Fundraiser for Humanitarian Aid	Hi all, we're initiating a fundraiser to aid families affected by conflicts. Your support is crucial in making a difference. Let's contribute together.
Proposal: Ethical Sourcing Guidelines	Hello Team, proposing ethical sourcing guidelines to align with our values and promote responsible business practices. Your thoughts?
Islamic Lecture Insights	Salaam friends, today's lecture was enlightening. It touched upon compassion and empathyâ€”essential virtues we should embrace. Let's discuss over coffee.
Boycott Awareness Drive: Join the Movement	Dear All, advocating for ethical consumerism amid the conflict. Let's raise awareness and choose brands aligned with our values. Let's take a stand!
Fast-Food Favorites Unveiled!	Hi pals, craving some fast-food goodness? Here are my top picks and must-try menu items. Bon appÃ©tit!
Volunteers Needed: Community Support Event	Hello, seeking volunteers for a community outreach event. Your dedication can impact lives positively. Let's volunteer for a noble cause!
Reflections on Faith and Unity	Hi there, today's reflection on unity and faith resonated deeply. Would love to hear your perspectives on these values.
Collaboration Opportunity: Community Engagement Project	Hi Team, proposing a project fostering community engagement. Let's brainstorm ideas and make a meaningful impact together.
Sign & Share: Petition for Humanitarian Aid	Hi friends, signing this petition can offer relief to affected regions. Let's unite and support those in need.
Consumer Responsibility: Ethical Choices Matter	Dear [Company], as a concerned consumer, I urge accountability and transparency regarding your practices amidst ongoing conflicts.
Stand Together: Community Event for Justice	Hi everyone, let's join hands for a community event advocating justice and equality. Your presence will make a significant impact!
Proposal: Corporate Social Responsibility Program	Hello Team, suggesting a CSR program to support marginalized communities. Let's discuss how we can contribute positively.
Thought-Provoking Lecture Discussion	Salaam friends, the lecture today delved into social responsibility. Excited to exchange thoughts and ideas over dinner. Join in!
Ethical Choices for a Better Tomorrow	Dear All, advocating for ethical consumerism amidst global conflicts. Let's be mindful of our choices and support ethical brands.
Fast-Food Feast Planning!	Hi pals, let's plan a fast-food feast at our favorite joint this weekend. Who's in for some good food and great company?
Collaborative Effort: Social Awareness Campaign	Hello, seeking collaborators for a social awareness campaign. Together, we can make a difference in our community.
Reflections on Compassion and Unity	Hi there, today's reflections on compassion sparked introspection. Let's share our views on fostering unity and compassion.
Joining Hands: Community Service Initiative	Hi Team, let's brainstorm ideas for a community service initiative. Your input can create a positive impact.
Sign & Share: Support for Humanitarian Aid	Hi friends, your signature can contribute to humanitarian aid efforts. Let's sign and share for a noble cause.
Request for Transparency: Ethical Concerns	Dear [Company], seeking clarity and transparency regarding your stand and practices in conflict-afflicted regions.
Invitation to Speak at a Social Justice Conference	Dear Siti, we are impressed by your dedication to social issues. We'd like to invite you as a guest speaker at our upcoming conference on social justice. Please let us know your availability.
Update on Palestine Relief Fund	Hello Siti, thank you for your contribution to the Palestine Relief Fund. Here's an update on how your donation has made a significant impact on the ground. Your support is greatly appreciated.
Confirmation of RSVP for Islamic Seminar	Dear Siti, thank you for confirming your attendance at the upcoming Islamic seminar. We look forward to your participation and insightful contributions to the discussions.
Company Policy Update Regarding Conflict-Affected Regions	Hi Siti, we're reaching out to inform you about our revised policies regarding conflict-affected regions. Your feedback and suggestions on ensuring ethical practices are valued.
Exclusive Offers at Halal Restaurants in Your Area	Hello Siti, discover exclusive deals and offers at Halal restaurants near you! As a supporter of Islamic establishments, we thought you might be interested in these offers.
Invitation to Join a Local Activism Group	Dear Siti, we've noticed your passion for social causes. We invite you to join our local activism group dedicated to creating positive change in our community. Your involvement will be invaluable.
Thank You for Your Feedback on Ethical Sourcing	Hi Siti, thank you for sharing your insights on ethical sourcing. We're considering your suggestions seriously as we aim to align our practices with ethical standards.
Confirmation of Registration for Fast-Food Loyalty Program	Hello Siti, your registration for the Fast-Food Loyalty Program is confirmed! Enjoy exclusive discounts and rewards at your favorite fast-food joints.
Invitation to Collaborate on a Charity Event	Dear Siti, we admire your dedication to community service. We'd love to collaborate with you on organizing a charity event for underprivileged children. Let's make a difference together.
Newsletter - Latest Developments in Conflict Zones	Hi Siti, here's our latest newsletter highlighting updates and developments in conflict zones. Stay informed about ongoing global issues and their impact.
'''
    prompt = "Human: \nBased on the list of emails:\n\n<email>\n" + email + "\n\nProfile this user by including their social views, risk tolerance, personality, provide long explanations\nAssistant:"
    # brt = boto3.client(service_name='bedrock-runtime', )
    modelId = 'anthropic.claude-v2'
        
    accept = 'application/json'
    contentType = 'application/json'

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 3000,
        "temperature": 0.1,
        "top_p": 0.9,
    })

    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())

    # text
    return(response_body.get('completion'))


def company_stance(company, is1, is2):
    prompt = f"""Human: \n
        Please provide the stance or performance of {company} on {is1} and {is2}. 

        Without words, Output only in a JSON format as follows:
        {{"{is1}": *answer*,
          "{is2}": *answer*
        }}

        \nAssistant:
    """

    return ai(2, prompt)

def find_issues():
    issue_prompt = "Human:\n" + settings.PROFILE + '''\nBased on the above, please summarise the two issues they feel most strongly about. Present in a JSON format: {"issue_interested1": *answer*,
                    "issue_interested2": *answer*,
                    }
                    Assistant:'''
    issue_ans = ai(1, issue_prompt)
    return [issue_ans["issue_interested1"], issue_ans["issue_interested2"]]

def company(request):
    settings.PROFILE = gen_profile()
    
    issues = find_issues()
    issue1 = issues[0]
    issue2 = issues[1]

    stance = company_stance("Nestle", issue1, issue2)
    stance1 = stance[issue1]
    stance2 = stance[issue2]




    if request.method == 'POST':
        user_input = request.POST['user_input']
        context = {'chatbot_output': chatbot(user_input),
                    "issue1": issue1,
                    "issue2": issue2,
                    "stance1": stance1,
                    "stance2": stance2}
        
        return render(request, "company/company.html", context)  
    else:

        context = {
        "issue1": issue1,
        "issue2": issue2,
        "stance1": stance1,
        "stance2": stance2
        }
        return render(request, "company/company.html", context)



import boto3
import json
import regex
from django.conf import settings


def json2dict(j):
    pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
    return json.loads("".join(pattern.findall(j)))


def ai(ver, prompt):
    brt = boto3.client(service_name='bedrock-runtime')
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
    email = '''Subject,Content
"Join the Climate Action Movement Today!", "Dear Wae Sern, Take a stand for the environment! Join our community-driven initiative to combat climate change and protect our planet. Your voice matters!"
"Invitation to a Human Rights Seminar", "Hi Wae Sern, You're invited to a seminar focusing on child labor issues and human rights violations. Join us to discuss and take action against these critical issues affecting our world."
"New Sustainable Investment Opportunity", "Hello Wae Sern, Discover a new investment opportunity aligned with your values! Our company prioritizes environmental sustainability and ethical practices. Learn more about our socially responsible investments."
"Urgent Petition: Stop Environmental Destruction", "Wae Sern, Help protect our forests! Sign our urgent petition to stop deforestation and preserve natural habitats. Every signature counts in the fight against environmental destruction."
"Newsletter: Eco-Friendly Lifestyle Tips", "Dear Wae Sern, Here are some practical tips for living a more eco-friendly life! From reducing plastic waste to adopting sustainable habits, every small change contributes to a greener planet."
"Support Ethical Brands: Exclusive Discounts Inside", "Hi Wae Sern, Explore ethical brands that prioritize fair labor practices and environmental sustainability. Enjoy exclusive discounts as a supporter of ethical consumerism."
"Update on Child Labor Legislation", "Wae Sern, Stay informed about recent developments in child labor laws! Here's an update on legislative efforts and initiatives aimed at ending child labor globally."
"Your Impact: Environmental Volunteer Opportunities", "Hello Wae Sern, Make a difference! Volunteer for environmental conservation projects in your area. Your passion for the environment can create real change."
"Webinar: Ethical Investing in a Changing World", "Hi Wae Sern, Join our webinar on ethical investing! Learn how to invest in companies that align with your values while maximizing financial returns."
"Call for Action: Protecting Endangered Species", "Wae Sern, Take action now! Join us in protecting endangered species from extinction. Your support can safeguard biodiversity and preserve our planet's natural heritage."
"Volunteer Opportunity: Environmental Cleanup Event", "Dear Wae Sern, Join us for an upcoming environmental cleanup event! Contribute to a cleaner environment and make a direct impact in your community."
"Your Impact: Supporting Fair Trade Initiatives", "Hi Wae Sern, Learn how your support for fair trade products empowers communities and ensures fair wages for workers. Every purchase makes a difference!"
"Breaking News: Global Climate Change Report", "Wae Sern, Stay informed! Read the latest global climate change report detailing the current state of our planet and the urgency for action."
"Take a Stand: Petition Against Ocean Pollution", "Join the fight against ocean pollution, Wae Sern! Sign our petition urging governments to implement stricter measures to protect our oceans."
"Invitation to Environmental Symposium", "Dear Wae Sern, You're invited to an environmental symposium featuring discussions on sustainability, renewable energy, and preserving natural resources."
"Ethical Investment Portfolio Analysis", "Hi Wae Sern, Receive a personalized analysis of ethical investment portfolios aligned with your values. Make informed investment decisions without compromising your beliefs."
"Action Needed: Protecting Indigenous Land Rights", "Wae Sern, Indigenous land rights are under threat. Take action now to support the protection of ancestral lands and indigenous communities."
"Newsletter: Advocacy Updates on Child Labor", "Stay updated on child labor advocacy efforts! Our newsletter covers recent developments and ways to advocate for children's rights globally."
"Join the Movement: Sustainable Fashion Revolution", "Hi Wae Sern, Be a part of the sustainable fashion revolution! Discover eco-friendly clothing brands and learn about ethical fashion practices."
"Webinar Invitation: Investing for Social Impact", "Join our webinar on investing for social impact! Explore how investments can create positive social change without compromising financial returns."
"Join Me in Supporting Ethical Investments", "Hi there! I've discovered some fantastic investment opportunities that align with our values. Let's chat about ethical investing and its positive impact!"
"Let's Take Action for Environmental Conservation", "Hey, I'm passionate about preserving our planet. Join me in volunteering for a local cleanup event this weekend. Together, we can make a difference!"
"Advocating for Child Rights - Join the Movement!", "Hey, I'm advocating against child labor and supporting organizations fighting for children's rights. Let's work together to make a change!"
"Discover Eco-Friendly Brands with Me", "Hi! I've found some awesome eco-friendly brands that prioritize sustainability. Let's explore and support them together!"
"Urgent: Sign the Petition to Protect Endangered Species", "Hey, I'm taking a stand against species extinction. Join me in signing this critical petition to protect endangered wildlife."
"Learn with Me: Climate Change and Solutions", "Hi, I'm diving into understanding climate change and its solutions. Let's learn together and brainstorm ways to combat this issue!"
"Volunteer Opportunity: Environmental Advocacy", "Hey! I'm volunteering for an environmental advocacy group. Join me in making a tangible impact in our community!"
"Raising Awareness: Human Rights Seminar", "Hi, I'm attending a seminar on human rights issues. Join me to learn and raise awareness about crucial global concerns!"
"Join the Discussion on Sustainable Living", "Hey, I'm hosting a discussion on sustainable living practices. Join me to share ideas and learn from each other's experiences!"
"Let's Make a Difference: Support Fair Trade", "Hi there! I'm supporting fair trade initiatives. Join me in advocating for fair wages and ethical practices worldwide!"
"Advocacy Alert: Support for Clean Energy Policies", "Dear Wae Sern, Add your voice to the call for clean energy policies! Advocate for renewable energy initiatives to combat climate change."
"Exclusive Access: Sustainable Investing Forum Pass", "Hi Wae Sern, Gain exclusive access to a sustainable investing forum! Network with industry leaders and learn about impactful investment strategies."
"Volunteer Spotlight: Environmental Activism Success Stories", "Wae Sern, Read inspiring stories of environmental activists making a difference. Get inspired and learn how you can contribute!"
"Join the Fight: Ending Modern-Day Slavery", "Take a stand against modern-day slavery, Wae Sern! Join our campaign to end human trafficking and support survivors."
"Newsletter: Ethical Supply Chain Practices", "Stay informed about ethical supply chain practices! Our newsletter highlights companies committed to fair labor and sustainable sourcing."
"Climate Action Rally in Your City", "Dear Wae Sern, Attend a climate action rally in your city! Stand with fellow activists and demand urgent action for a sustainable future."
"Empowerment Through Education: Sponsor a Child's Education", "Wae Sern, Support a child's education and break the cycle of poverty. Learn how you can sponsor a child's schooling."
"Webinar Invitation: Environmental Policy and Advocacy", "Join our webinar on environmental policy and advocacy! Understand the importance of policy changes in environmental conservation."
"Calling All Changemakers: Social Impact Innovation Challenge", "Hi Wae Sern, Participate in a social impact innovation challenge! Showcase your ideas for solving pressing social issues."
"Newsletter: Updates on Endangered Species Conservation", "Stay updated on endangered species conservation efforts! Learn about successes and ongoing challenges in protecting endangered wildlife."
'''
    prompt = "Human: \nBased on the list of emails:\n\n<email>\n" + email + "\n\nProfile this user by including their social views, risk tolerance, personality, provide long explanations\nAssistant:"
    brt = boto3.client(service_name='bedrock-runtime')
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
        {{"{is1}": answer,
          "{is2}": answer
        }}

        \nAssistant:
    """

    return ai(2, prompt)

def find_issues():
    issue_prompt = "Human:\n" + settings.PROFILE + '''\nBased on the above, please summarise the two issues they feel most strongly about. Present in a JSON format: {"issue_interested1": answer,
                    "issue_interested2": answer,
                    }
                    Assistant:'''
    issue_ans = ai(1, issue_prompt)
    return [issue_ans["issue_interested1"], issue_ans["issue_interested2"]]

def gen_portfolio():
    profile = settings.PROFILE
    prompt = f'''Human:\n
        {profile}\n
        Based on the above, recommed two stocks in a JSON format:
        {{
        "stock1companyname": answer,
        "stock1ticker": answer,
        "stock1percentage": answer,
        "stock1reason1": answer,
        "stock1reason2": answer,
        "stock1reason3": answer,
        "stock2companyname": answer,
        "stock2ticker": answer,
        "stock2percentage": answer,
        "stock2reason1": answer,
        "stock2reason2": answer,
        "stock2reason3": answer,
        }}
        \n
        Assistant:\n
    '''

    return ai(2, prompt)

def startup():
    settings.PROFILE = gen_profile()
    
    settings.ISSUES = find_issues()
    issue1 = settings.ISSUES[0]
    issue2 = settings.ISSUES[1]

    settings.PORTFOLIO = gen_portfolio()

    settings.STANCES = company_stance("Nestle", issue1, issue2)

startup()
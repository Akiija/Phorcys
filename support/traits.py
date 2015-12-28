import math, os, random

pos = [
	'Active',
	'Adaptable',
	'Adventurous',
	'Alert',
	'Allocentric',
	'Amiable',
	'Articulate',
	'Athletic',
	'Attractive',
	'Benevolent',
	'Brilliant',
	'Calm',
	'Captivating',
	'Caring',
	'Charismatic',
	'Cheerful',
	'Clever',
	'Compassionate',
	'Conciliatory',
	'Confident',
	'Conscientious',
	'Considerate',
	'Contemplative',
	'Cooperative',
	'Courageous',
	'Courteous',
	'Creative',
	'Cultured',
	'Curious',
	'Daring',
	'Debonair',
	'Decent',
	'Decisive',
	'Dedicated',
	'Dignified',
	'Disciplined',
	'Discreet',
	'Dramatic',
	'Dutiful',
	'Earnest',
	'Ebullient',
	'Efficient',
	'Elegant',
	'Eloquent',
	'Empathetic',
	'Energetic',
	'Enthusiastic',
	'Faithful',
	'Farsighted',
	'Felicific',
	'Firm',
	'Flexible',
	'Focused',
	'Forceful',
	'Forgiving',
	'Forthright',
	'Freethinking',
	'Friendly',
	'Fun-loving',
	'Gallant',
	'Generous',
	'Gentle',
	'Genuine',
	'Good-natured',
	'Gracious',
	'Hardworking',
	'Hearty',
	'Helpful',
	'Heroic',
	'High-minded',
	'Honest',
	'Honorable',
	'Humble',
	'Humorous',
	'Idealistic',
	'Imaginative',
	'Incisive',
	'Incorruptible',
	'Independent',
	'Individualistic',
	'Innovative',
	'Inoffensive',
	'Insightful',
	'Insouciant',
	'Intelligent',
	'Intuitive',
	'Kind',
	'Knowledgeable',
	'Leaderly',
	'Leisurely',
	'Logical',
	'Lovable',
	'Loyal',
	'Lyrical',
	'Magnanimous',
	'Many-sided',
	'Masculine',
	'Mature',
	'Methodical',
	'Meticulous',
	'Modest',
	'Neat',
	'Nonauthoritarian',
	'Objective',
	'Observant',
	'Open',
	'Optimistic',
	'Orderly',
	'Organized',
	'Passionate',
	'Patient',
	'Patriotic',
	'Peaceful',
	'Perceptive',
	'Perfectionist',
	'Personable',
	'Persuasive',
	'Planful',
	'Playful',
	'Polished',
	'Popular',
	'Practical',
	'Precise',
	'Principled',
	'Profound',
	'Protean',
	'Protective',
	'Providential',
	'Prudent',
	'Punctual',
	'Purposeful',
	'Rational',
	'Realistic',
	'Reflective',
	'Relaxed',
	'Reliable',
	'Resourceful',
	'Respectful',
	'Responsible',
	'Responsive',
	'Reverential',
	'Romantic',
	'Rustic',
	'Sage',
	'Sane',
	'Scholarly',
	'Scrupulous',
	'Secure',
	'Selfless',
	'Self-critical',
	'Self-defacing',
	'Self-denying',
	'Self-reliant',
	'Self-sufficient',
	'Sensitive',
	'Sentimental',
	'Seraphic',
	'Serious',
	'Sexy',
	'Sharing',
	'Shrewd',
	'Simple',
	'Skillful',
	'Sober',
	'Sociable',
	'Sophisticated',
	'Spontaneous',
	'Sporting',
	'Stable',
	'Steadfast',
	'Steady',
	'Stoic',
	'Strong',
	'Studious',
	'Suave',
	'Subtle',
	'Sweet',
	'Sympathetic',
	'Systematic',
	'Tasteful',
	'Teacherly',
	'Thorough',
	'Tidy',
	'Tolerant',
	'Tractable',
	'Trusting',
	'Uncomplaining',
	'Understanding',
	'Undogmatic',
	'Unfoolable',
	'Upright',
	'Urbane',
	'Venturesome',
	'Vivacious',
	'Warm',
	'Well-bred',
	'Well-read',
	'Well-rounded',
	'Wise',
	'Witty',
	'Youthful']

def disp_pos():
	print('Think of a someone...', pos[random.randint(0, len(pos)-1)])

neu = [
	'Absentminded',
 	'Aggressive',
 	'Ambitious',
 	'Amusing',
 	'Artful',
 	'Ascetic',
 	'Authoritarian',
 	'Big-thinking',
 	'Boyish',
 	'Breezy',
 	'Businesslike',
 	'Busy',
 	'Casual',
 	'Cerebral',
 	'Chummy',
 	'Circumspect',
 	'Competitive',
 	'Complex',
 	'Confidential',
 	'Conservative',
 	'Contradictory',
 	'Crisp',
 	'Cute',
 	'Deceptive',
 	'Determined',
 	'Dominating',
 	'Dreamy',
 	'Driving',
 	'Droll',
 	'Dry',
 	'Earthy',
 	'Effeminate',
 	'Emotional',
 	'Enigmatic',
 	'Experimental',
 	'Familial',
 	'Folksy',
 	'Formal',
 	'Freewheeling',
 	'Frugal',
 	'Glamorous',
 	'Guileless',
 	'High-spirited',
 	'Hurried',
 	'Hypnotic',
 	'Iconoclastic',
 	'Idiosyncratic',
 	'Impassive',
 	'Impersonal',
 	'Impressionable',
 	'Intense',
 	'Invisible',
 	'Irreligious',
 	'Irreverent',
 	'Maternal',
 	'Mellow',
 	'Modern',
 	'Moralistic',
 	'Mystical',
 	'Neutral',
 	'Noncommittal',
 	'Noncompetitive',
 	'Obedient',
 	'Old-fashioned',
 	'Ordinary',
 	'Outspoken',
 	'Paternalistic',
 	'Physical',
 	'Placid',
 	'Political',
 	'Predictable',
 	'Preoccupied',
 	'Private',
 	'Progressive',
 	'Proud',
 	'Pure',
 	'Questioning',
 	'Quiet',
 	'Religious',
 	'Reserved',
 	'Restrained',
 	'Retiring',
 	'Sarcastic',
 	'Self-conscious',
 	'Sensual',
 	'Skeptical',
 	'Smooth',
 	'Soft',
 	'Solemn',
 	'Solitary',
 	'Stern',
 	'Stolid',
 	'Strict',
 	'Stubborn',
 	'Stylish',
 	'Soft',
 	'Tough',
 	'Unaggressive',
 	'Unambitious',
 	'Unceremonious',
 	'Unchanging',
 	'Undemanding',
 	'Unfathomable',
 	'Unhurried',
 	'Uninhibited',
 	'Unpatriotic',
 	'Unpredictable',
 	'Unreligious',
 	'Unsentimental',
 	'Whimsical']

def disp_neu():
	print('Think of someone...', neu[random.randint(0, len(neu)-1)])

neg = [
	'Abrasive',
	'Abrupt',
	'Agonizing',
	'Aimless',
	'Airy',
	'Aloof',
	'Amoral',
	'Angry',
	'Anxious',
	'Apathetic',
	'Arbitrary',
	'Argumentative',
	'Arrogant',
	'Artificial',
	'Asocial',
	'Assertive',
	'Astigmatic',
	'Barbaric',
	'Bewildered',
	'Bizarre',
	'Bland',
	'Blunt',
	'Boisterous',
	'Brittle',
	'Brutal',
	'Calculating',
	'Callous',
	'Cantankerous',
	'Careless',
	'Cautious',
	'Charmless',
	'Childish',
	'Clumsy',
	'Coarse',
	'Cold',
	'Colorless',
	'Complacent',
	'Complaintive',
	'Compulsive',
	'Conceited',
	'Condemnatory',
	'Conformist',
	'Confused',
	'Contemptible',
	'Conventional',
	'Cowardly',
	'Crafty',
	'Crass',
	'Crazy',
	'Criminal',
	'Critical',
	'Crude',
	'Cruel',
	'Cynical',
	'Decadent',
	'Deceitful',
	'Delicate',
	'Demanding',
	'Dependent',
	'Desperate',
	'Destructive',
	'Devious',
	'Difficult',
	'Dirty',
	'Disconcerting',
	'Discontented',
	'Discouraging',
	'Discourteous',
	'Dishonest',
	'Disloyal',
	'Disobedient',
	'Disorderly',
	'Disorganized',
	'Disputatious',
	'Disrespectful',
	'Disruptive',
	'Dissolute',
	'Dissonant',
	'Distractible',
	'Disturbing',
	'Dogmatic',
	'Domineering',
	'Dull'
	'Easily Discouraged',
	'Egocentric',
	'Enervated',
	'Envious',
	'Erratic',
	'Escapist',
	'Excitable',
	'Expedient',
	'Extravagant',
	'Extreme',
	'Faithless',
	'False',
	'Fanatical',
	'Fanciful',
	'Fatalistic',
	'Fawning',
	'Fearful',
	'Fickle',
	'Fiery',
	'Fixed',
	'Flamboyant',
	'Foolish',
	'Forgetful',
	'Fraudulent',
	'Frightening',
	'Frivolous',
	'Gloomy',
	'Graceless',
	'Grand',
	'Greedy',
	'Grim',
	'Gullible',
	'Hateful',
	'Haughty',
	'Hedonistic',
	'Hesitant',
	'Hidebound',
	'High-handed',
	'Hostile',
	'Ignorant',
	'Imitative',
	'Impatient',
	'Impractical',
	'Imprudent',
	'Impulsive',
	'Inconsiderate',
	'Incurious',
	'Indecisive',
	'Indulgent',
	'Inert',
	'Inhibited',
	'Insecure',
	'Insensitive',
	'Insincere',
	'Insulting',
	'Intolerant',
	'Irascible',
	'Irrational',
	'Irresponsible',
	'Irritable',
	'Lazy',
	'Libidinous',
	'Loquacious',
	'Malicious',
	'Mannered',
	'Mannerless',
	'Mawkish',
	'Mealymouthed',
	'Mechanical',
	'Meddlesome',
	'Melancholic',
	'Meretricious',
	'Messy',
	'Miserable',
	'Miserly',
	'Misguided',
	'Mistaken',
	'Money-minded',
	'Monstrous',
	'Moody',
	'Morbid',
	'Muddle-headed',
	'Naive',
	'Narcissistic',
	'Narrow',
	'Narrow-minded',
	'Natty',
	'Negativistic',
	'Neglectful',
	'Neurotic',
	'Nihilistic',
	'Obnoxious',
	'Obsessive',
	'Obvious',
	'Odd',
	'Offhand',
	'One-dimensional',
	'One-sided',
	'Opinionated',
	'Opportunistic',
	'Oppressed',
	'Outrageous',
	'Overimaginative',
	'Paranoid',
	'Passive',
	'Pedantic',
	'Perverse',
	'Petty',
	'Pharissical',
	'Phlegmatic',
	'Plodding',
	'Pompous',
	'Possessive',
	'Power-hungry',
	'Predatory',
	'Prejudiced',
	'Presumptuous',
	'Pretentious',
	'Prim',
	'Procrastinating',
	'Profligate',
	'Provocative',
	'Pugnacious',
	'Puritanical',
	'Quirky',
	'Reactionary',
	'Reactive',
	'Regimental',
	'Regretful',
	'Repentant',
	'Repressed',
	'Resentful',
	'Ridiculous',
	'Rigid',
	'Ritualistic',
	'Rowdy',
	'Ruined',
	'Sadistic',
	'Sanctimonious',
	'Scheming',
	'Scornful',
	'Secretive',
	'Sedentary',
	'Selfish',
	'Self-indulgent',
	'Shallow',
	'Shortsighted',
	'Shy',
	'Silly',
	'Single-minded',
	'Sloppy',
	'Slow',
	'Sly',
	'Small-thinking',
	'Softheaded',
	'Sordid',
	'Steely',
	'Stiff',
	'Strong-willed',
	'Stupid',
	'Submissive',
	'Superficial',
	'Superstitious',
	'Suspicious',
	'Tactless',
	'Tasteless',
	'Tense',
	'Thievish',
	'Thoughtless',
	'Timid',
	'Transparent',
	'Treacherous',
	'Trendy',
	'Troublesome',
	'Unappreciative',
	'Uncaring',
	'Uncharitable',
	'Unconvincing',
	'Uncooperative',
	'Uncreative',
	'Uncritical',
	'Unctuous',
	'Undisciplined',
	'Unfriendly',
	'Ungrateful',
	'Unhealthy',
	'Unimaginative',
	'Unimpressive',
	'Unlovable',
	'Unpolished',
	'Unprincipled',
	'Unrealistic',
	'Unreflective',
	'Unreliable',
	'Unrestrained',
	'Unstable',
	'Vacuous',
	'Vague',
	'Venal',
	'Venomous',
	'Vindictive',
	'Vulnerable',
	'Weak'
	'Weak-willed',
	'Well-meaning',
	'Willful',
	'Wishful',
	'Zany']

def disp_neg():
	print('Think of someone...', neg[random.randint(0, len(neg)-1)])

switcher = {
	'pos' : disp_pos,
	'neu' : disp_neu,
	'neg' : disp_neg}

def main():
	print('Sounds like you need an idea.\n-------------')
	info = input('>>> ')
	os.system('cls')

	while(info != 'n'):
		while(info != 'n'):
			temp = switcher.get(info)
			temp()
			info = input('>>> ')

		print('\n\nNeed another idea?\n-------------')
		info = input('>>> ')
		os.system('cls')

	print('Oh... okay then. Bye!')

if __name__ == '__main__':
	main()

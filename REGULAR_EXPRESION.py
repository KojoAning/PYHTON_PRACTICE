import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
aaaaaaaaiii
aiiiiiiiiiii
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiin'''

'''findall: It finds all search for matches and print resultant in the form of a list.
search: It works the same as a findall, but the resultant is a matched object, if any found.
split: The split function splits the string from every matched into two new strings.
sub: The sub-function works exactly like a replace function in notepad or MS Word, it replaces the original word, 
with a word of our choice.
finditer: The finditer yields an iterator as a resultant with all the objects that match the one we sent it , 
finditer supports more attributes than any other function defined above. It also provides more details related to the matched 
object. So, most of the examples we are going to see next will contain a finditer function in them.'''


# pattern = re.compile(r'.')
# pattern = re.compile(r'fass') # >>> fass
# pattern = re.compile(r'.adm')
# pattern = re.compile(r'^Tata') # ^- statrt with
# pattern = re.compile(r'Tata$') # & Ends with
# pattern = re.compile(r'iin$') # & Ends with
# pattern = re.compile(r'ai*') #  (i)* Zero or more occurrences
# pattern = re.compile(r'a*i')# (a)* Zero or more occurrences
# pattern = re.compile(r'a*i*') # (a)* Zero or more occurrences , (i)* Zero or more occurrences
# pattern = re.compile(r'ai+') #+ One or more occurrences
# pattern = re.compile(r'ai{2}') # exactly the {given} no the occerance
# pattern =  re.compile(r'ai{2}|Fax') # | gives us either the 1st argument or 2nd


# special sequence
# pattern = re.compile(r'\ATata') # \A Returns a match if the specified characters are at the beginning of the string
# pattern = re.compile(r'\bFax') # \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
# pattern = re.compile(r'Fax\b')
# pattern = re.compile(r'27\b')




matches  = pattern.finditer(mystr)
for match in matches:
    print(match)
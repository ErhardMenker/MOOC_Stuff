# Copy in xml manually because there is no indication about how to
# import using urllib.

input = '''
<commentinfo>
<note>
This file contains the actual data for your assignment - good luck!
</note>
<comments>
<comment>
<name>Casey</name>
<count>99</count>
</comment>
<comment>
<name>Mariena</name>
<count>98</count>
</comment>
<comment>
<name>Pagan</name>
<count>97</count>
</comment>
<comment>
<name>Cassandra</name>
<count>94</count>
</comment>
<comment>
<name>Amelka</name>
<count>94</count>
</comment>
<comment>
<name>Carlos</name>
<count>91</count>
</comment>
<comment>
<name>Dionne</name>
<count>90</count>
</comment>
<comment>
<name>Gabriele</name>
<count>87</count>
</comment>
<comment>
<name>Hollee</name>
<count>85</count>
</comment>
<comment>
<name>Arshjoyat</name>
<count>84</count>
</comment>
<comment>
<name>Matteo</name>
<count>84</count>
</comment>
<comment>
<name>Aurelia</name>
<count>79</count>
</comment>
<comment>
<name>Elissa</name>
<count>78</count>
</comment>
<comment>
<name>Mischa</name>
<count>75</count>
</comment>
<comment>
<name>Rishi</name>
<count>70</count>
</comment>
<comment>
<name>Ayeesha</name>
<count>70</count>
</comment>
<comment>
<name>Siobhan</name>
<count>69</count>
</comment>
<comment>
<name>Alicia</name>
<count>65</count>
</comment>
<comment>
<name>Keilee</name>
<count>65</count>
</comment>
<comment>
<name>Nelly</name>
<count>60</count>
</comment>
<comment>
<name>Kaiya</name>
<count>59</count>
</comment>
<comment>
<name>Calice</name>
<count>57</count>
</comment>
<comment>
<name>Telise</name>
<count>56</count>
</comment>
<comment>
<name>Shakeira</name>
<count>53</count>
</comment>
<comment>
<name>Hussnain</name>
<count>52</count>
</comment>
<comment>
<name>Teighen</name>
<count>52</count>
</comment>
<comment>
<name>Derren</name>
<count>48</count>
</comment>
<comment>
<name>Camryn</name>
<count>47</count>
</comment>
<comment>
<name>Lilah</name>
<count>46</count>
</comment>
<comment>
<name>Obosa</name>
<count>46</count>
</comment>
<comment>
<name>Levy</name>
<count>36</count>
</comment>
<comment>
<name>Keyra</name>
<count>36</count>
</comment>
<comment>
<name>Maximillian</name>
<count>34</count>
</comment>
<comment>
<name>Bryoni</name>
<count>33</count>
</comment>
<comment>
<name>Harold</name>
<count>32</count>
</comment>
<comment>
<name>Hariot</name>
<count>32</count>
</comment>
<comment>
<name>Hamid</name>
<count>30</count>
</comment>
<comment>
<name>Deshawn</name>
<count>28</count>
</comment>
<comment>
<name>Agnieszka</name>
<count>27</count>
</comment>
<comment>
<name>Sayad</name>
<count>25</count>
</comment>
<comment>
<name>Rania</name>
<count>22</count>
</comment>
<comment>
<name>Sahana</name>
<count>19</count>
</comment>
<comment>
<name>Rhiannin</name>
<count>18</count>
</comment>
<comment>
<name>Daumantas</name>
<count>18</count>
</comment>
<comment>
<name>Carris</name>
<count>17</count>
</comment>
<comment>
<name>Aiyana</name>
<count>16</count>
</comment>
<comment>
<name>Kayla</name>
<count>12</count>
</comment>
<comment>
<name>Ivana</name>
<count>8</count>
</comment>
<comment>
<name>Talha</name>
<count>5</count>
</comment>
<comment>
<name>Christian</name>
<count>3</count>
</comment>
</comments>
</commentinfo>
'''

import urllib
import xml.etree.ElementTree as ET

# create a tree bounded in the 'commentinfo' parent
stuff = ET.fromstring(input)
# create a list of all the tags within the 'comments' and then within the 'comment' tags.
lst = stuff.findall('comments/comment')

sum = 0
# iterate through each line in the list, extracting the corresponding node to the count tag.
for item in lst:
    x = item.find('count').text
    count = int(x)
    sum += count
print(sum)


    


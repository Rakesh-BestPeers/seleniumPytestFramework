***settings***
library    requests


***variable***
${base_url}   http://restapi.demoqa.com
${city}        delhi

***test cases ***
get_weatherInfo()
 create session myssion   ${base_url}
 ${response} = get request myssion   /utilities/weather/city/${city}
 log to console    ${response.status_code}
 log to console    ${response.content}
 log to console    ${response.header}
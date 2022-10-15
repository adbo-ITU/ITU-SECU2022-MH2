# Security 1, mandatory hand-in 2

By Adrian Borup (adbo@itu.dk).

## Dependencies

I use `pyaes` for AES encryption. Install it with `pip`:

```sh
pip install pyaes
```

## Instructions for running

### How to understand the logs?

- `[NETWORK SEND]` and `[NETWORK RECV]` represent information sent in plaintext over the network. Any eavesdropper can read this directly.
- `[SEND: TO ENCRYPT]` and `[RECV: DECRYPTED]` represent information that will be encrypted, have a MAC added, and then sent over the network.

### Running it

From one terminal:

```log
$ python player.py
[DEBUG] My long-term private key: 3202
[DEBUG] My long-term public key: 527
[INFO] Other player is not hosting - I will be the server.
[INFO] Waiting for other player to connect...
[INFO] Player connected from 127.0.0.1:50203.
[DEBUG] Diffie-Hellman key pair - Private: 5650, Public: 5000
[DEBUG] [NETWORK RECV] {"message":"{\"recipient\":\"server\",\"sender\":\"client\",\"dh_public\":\"2600\"}","signature":{"r":"2457","s":"3751"}}
[DEBUG] [NETWORK SEND] {"message":"{\"recipient\":\"client\",\"sender\":\"server\",\"dh_public\":\"5650\"}","signature":{"r":"2859","s":"934"}}
[DEBUG] Authenticated key exchange completed with client. Shared key: 3505
[DEBUG] [NETWORK RECV] b'\x93\xfa#\xd9%\x97\x1c\xd2\xf1,\x0e\'\x0f5\x7fb\xfd@ -\x8c\xa8\x07y\nJ}\x1d\xcbF\xc6\x07\xc4\xd9\xf8\\\x1c\xef\xbaMS\x85\x8a\xdfw\xe6=\x84\xeb{\xa2A\xa2\xb9!\xb8\xdd\xfe\x8chOa\xbd\x12\xd8 -\xc46\x18\xd3\xbf`\xd4&9|,\r\xae\x96y\xd0a\x84(,\x84"\xd3\xc3\xacG\\F5\x1f\xe3\x13b>9\xea\x84\n#M\xa1$\xa9\xc7>\xfa\x98y\xfev\xb3?\x95\x8b\xca\x80\x97V\xca\xe9\x9f'
[DEBUG] [RECV: DECRYPTED] Message: '542403dd57e984b5b4f82758a60fd7550bc7d5b6d499e5558d8c2aa27bc4330d', MAC: '525396f11cc0575ba4459cec4d0c0b29c5fd9bab9cd99bfee73580840695ff44'
[DEBUG] [SEND: TO ENCRYPT] Message: '3', MAC: '4d7285c0d0cd099efbc41c2ff903dede1ece28fd86d9fd13e1eaf233c38f62e7'
[DEBUG] [NETWORK SEND] b"\x95\xfau\xda'\x9cM\xd5\xf4\x7f[}S1$n\xfa\x12$v\x8a\xaeQs\r\x1atK\x9c\x15\x96V\x91\x8a\xfe\x08\x1d\xe8\xe0\x1dS\x89\x85\x82+\xb5l\x80\xe0z\xabG\xf1\xber\xb9\xd9\xff\xdcd\x1ad\xbf\x13\xda"
[DEBUG] [NETWORK RECV] b"\x90\xee(\xd5#\x93J\x87\xf2,Y'\x0f5-f\xa6L~ \x8b\xa8\nwXOtI\x96B\xc1\x03\xcd\x89\xa3XO\xe2\xe1J\x00\x88\x8b\xd1!\xea8\x89\xe0.\xa8\x13\xa1\xeep\xb2\xde\xac\xd6dLb\xbbE\xdf (\xc19\x1d\x81\xbff\x87w?p(\x0b\xfa\xc1~\x871\x89*p\xd7%\x80\xc1\xff\x15\t@nO\xb5M?a9\xba\xdfUuL\xf9\x7f\xfc\x90i\xfd\xcbx\xa9y\xe75\x97\x89\x9f\x80\xc4\x03\x9c\xeb\x9d\x17\x1c\xacV{\x1c\xb5\x9aR\x9c\xd1\x94,8\xb9"
[DEBUG] [RECV: DECRYPTED] Message: '6 98672167298401988557863392932192837891798739083121160840980063220663417026933', MAC: '663ce4a903720b74b3c89fb19f5eab712bd2b7d262c9f3066561caa821014252'
[INFO] Commitment matches roll.
[INFO] Roll result: 6
[DEBUG] [SEND: TO ENCRYPT] Message: '20b99afafe423bf1a8e474e21eab74ee3628b031f9fdd84ac5358553adb8e435', MAC: '9c8e55ead00e7d21d62044239cc89cd3363f864e02ab5101a397d4e5886b30e9'
[DEBUG] [NETWORK SEND] b'\x94\xfes\xd4,\xc5\x1e\xd7\xa2~_,\x04c{f\xfeL#!\x89\xabWsZ\x19,\x19\x98E\x96W\xc7\x8d\xa9S\x1a\xea\xebJQ\x88\xd5\x82v\xeb<\xd0\xb0*\xa9\x17\xa8\xedu\xb9\x8b\xf8\x8dd\x19f\xbeC\xd4q \x92:\x1b\xd0\xef5\x87ul~\x7f\n\xfd\x93{\xd6d\x89\x7f{\xd4/\xd4\x90\xf7N]\x10?O\xe0F`?m\xbf\x83\x03rH\xfa(\xfa\x91j\xfe\x9cs\xfc*\xb7b\x94\x83\xc4\x8f\xc0\x03\x9c\xb8\x92'
[DEBUG] [NETWORK RECV] b"\x95\xfau\xda'\x9cM\xd5\xf4\x7f[}S1$n\xfa\x12$v\x8a\xaeQs\r\x1atK\x9c\x15\x96V\x91\x8a\xfe\x08\x1d\xe8\xe0\x1dS\x89\x85\x82+\xb5l\x80\xe0z\xabG\xf1\xber\xb9\xd9\xff\xdcd\x1ad\xbf\x13\xda"
[DEBUG] [RECV: DECRYPTED] Message: '3', MAC: '4d7285c0d0cd099efbc41c2ff903dede1ece28fd86d9fd13e1eaf233c38f62e7'
[DEBUG] [SEND: TO ENCRYPT] Message: '4 111830250815309484304363362494622882058705163042921030329216776413649332647343', MAC: '7214b3e3d54a030bd8e364e036817a63b06f821447654faf99a19d2c15e5d188'
[DEBUG] [NETWORK SEND] b'\x92\xee \xdc$\x9cK\x86\xf6.[&\x064.g\xa6@~!\x8d\xaf\x06r]O~M\x9dE\xca\x06\xc2\x89\xa9S@\xe8\xe8N\x0f\x86\x83\xd3#\xe5;\x81\xe7-\xa3\x10\xa1\xe8s\xba\xd9\xae\xd6nMd\xbaA\xdb&)\xc49\x1a\x8c\xbdb\x85s=~(\x0c\xff\xc0\x7f\xd5`\xdfx,\xd4r\x82\xc7\xaeG\rDn\x18\xee\x1051o\xee\xd6\x00v\x11\xa9*\xaa\x97h\xfd\x9f|\xadv\xb16\x95\x8f\xcb\x8f\x97\x04\xca\xbc\xcd\x1b\x13\xfc\x04#\x19\xbf\xcbR\x99\x85\x95z<\xb3-'
[INFO] Roll result: 2
[INFO] Player disconnected.
[INFO] Game is finished.
[DEBUG] Distribution of rolls: [0, 1, 0, 0, 0, 1]
```

From another terminal:

```log
$ python player.py
[DEBUG] My long-term private key: 3613
[DEBUG] My long-term public key: 5496
[INFO] Other player is hosting - I will start.
[DEBUG] Diffie-Hellman key pair - Private: 2600, Public: 5640
[DEBUG] [NETWORK SEND] {"message":"{\"recipient\":\"server\",\"sender\":\"client\",\"dh_public\":\"2600\"}","signature":{"r":"2457","s":"3751"}}
[DEBUG] [NETWORK RECV] {"message":"{\"recipient\":\"client\",\"sender\":\"server\",\"dh_public\":\"5650\"}","signature":{"r":"2859","s":"934"}}
[DEBUG] Authenticated key exchange completed with server. Shared key: 3505
[DEBUG] [SEND: TO ENCRYPT] Message: '542403dd57e984b5b4f82758a60fd7550bc7d5b6d499e5558d8c2aa27bc4330d', MAC: '525396f11cc0575ba4459cec4d0c0b29c5fd9bab9cd99bfee73580840695ff44'
[DEBUG] [NETWORK SEND] b'\x93\xfa#\xd9%\x97\x1c\xd2\xf1,\x0e\'\x0f5\x7fb\xfd@ -\x8c\xa8\x07y\nJ}\x1d\xcbF\xc6\x07\xc4\xd9\xf8\\\x1c\xef\xbaMS\x85\x8a\xdfw\xe6=\x84\xeb{\xa2A\xa2\xb9!\xb8\xdd\xfe\x8chOa\xbd\x12\xd8 -\xc46\x18\xd3\xbf`\xd4&9|,\r\xae\x96y\xd0a\x84(,\x84"\xd3\xc3\xacG\\F5\x1f\xe3\x13b>9\xea\x84\n#M\xa1$\xa9\xc7>\xfa\x98y\xfev\xb3?\x95\x8b\xca\x80\x97V\xca\xe9\x9f'
[DEBUG] [NETWORK RECV] b"\x95\xfau\xda'\x9cM\xd5\xf4\x7f[}S1$n\xfa\x12$v\x8a\xaeQs\r\x1atK\x9c\x15\x96V\x91\x8a\xfe\x08\x1d\xe8\xe0\x1dS\x89\x85\x82+\xb5l\x80\xe0z\xabG\xf1\xber\xb9\xd9\xff\xdcd\x1ad\xbf\x13\xda"
[DEBUG] [RECV: DECRYPTED] Message: '3', MAC: '4d7285c0d0cd099efbc41c2ff903dede1ece28fd86d9fd13e1eaf233c38f62e7'
[DEBUG] [SEND: TO ENCRYPT] Message: '6 98672167298401988557863392932192837891798739083121160840980063220663417026933', MAC: '663ce4a903720b74b3c89fb19f5eab712bd2b7d262c9f3066561caa821014252'
[DEBUG] [NETWORK SEND] b"\x90\xee(\xd5#\x93J\x87\xf2,Y'\x0f5-f\xa6L~ \x8b\xa8\nwXOtI\x96B\xc1\x03\xcd\x89\xa3XO\xe2\xe1J\x00\x88\x8b\xd1!\xea8\x89\xe0.\xa8\x13\xa1\xeep\xb2\xde\xac\xd6dLb\xbbE\xdf (\xc19\x1d\x81\xbff\x87w?p(\x0b\xfa\xc1~\x871\x89*p\xd7%\x80\xc1\xff\x15\t@nO\xb5M?a9\xba\xdfUuL\xf9\x7f\xfc\x90i\xfd\xcbx\xa9y\xe75\x97\x89\x9f\x80\xc4\x03\x9c\xeb\x9d\x17\x1c\xacV{\x1c\xb5\x9aR\x9c\xd1\x94,8\xb9"
[INFO] Roll result: 6
[DEBUG] [NETWORK RECV] b'\x94\xfes\xd4,\xc5\x1e\xd7\xa2~_,\x04c{f\xfeL#!\x89\xabWsZ\x19,\x19\x98E\x96W\xc7\x8d\xa9S\x1a\xea\xebJQ\x88\xd5\x82v\xeb<\xd0\xb0*\xa9\x17\xa8\xedu\xb9\x8b\xf8\x8dd\x19f\xbeC\xd4q \x92:\x1b\xd0\xef5\x87ul~\x7f\n\xfd\x93{\xd6d\x89\x7f{\xd4/\xd4\x90\xf7N]\x10?O\xe0F`?m\xbf\x83\x03rH\xfa(\xfa\x91j\xfe\x9cs\xfc*\xb7b\x94\x83\xc4\x8f\xc0\x03\x9c\xb8\x92'
[DEBUG] [RECV: DECRYPTED] Message: '20b99afafe423bf1a8e474e21eab74ee3628b031f9fdd84ac5358553adb8e435', MAC: '9c8e55ead00e7d21d62044239cc89cd3363f864e02ab5101a397d4e5886b30e9'
[DEBUG] [SEND: TO ENCRYPT] Message: '3', MAC: '4d7285c0d0cd099efbc41c2ff903dede1ece28fd86d9fd13e1eaf233c38f62e7'
[DEBUG] [NETWORK SEND] b"\x95\xfau\xda'\x9cM\xd5\xf4\x7f[}S1$n\xfa\x12$v\x8a\xaeQs\r\x1atK\x9c\x15\x96V\x91\x8a\xfe\x08\x1d\xe8\xe0\x1dS\x89\x85\x82+\xb5l\x80\xe0z\xabG\xf1\xber\xb9\xd9\xff\xdcd\x1ad\xbf\x13\xda"
[DEBUG] [NETWORK RECV] b'\x92\xee \xdc$\x9cK\x86\xf6.[&\x064.g\xa6@~!\x8d\xaf\x06r]O~M\x9dE\xca\x06\xc2\x89\xa9S@\xe8\xe8N\x0f\x86\x83\xd3#\xe5;\x81\xe7-\xa3\x10\xa1\xe8s\xba\xd9\xae\xd6nMd\xbaA\xdb&)\xc49\x1a\x8c\xbdb\x85s=~(\x0c\xff\xc0\x7f\xd5`\xdfx,\xd4r\x82\xc7\xaeG\rDn\x18\xee\x1051o\xee\xd6\x00v\x11\xa9*\xaa\x97h\xfd\x9f|\xadv\xb16\x95\x8f\xcb\x8f\x97\x04\xca\xbc\xcd\x1b\x13\xfc\x04#\x19\xbf\xcbR\x99\x85\x95z<\xb3-'
[DEBUG] [RECV: DECRYPTED] Message: '4 111830250815309484304363362494622882058705163042921030329216776413649332647343', MAC: '7214b3e3d54a030bd8e364e036817a63b06f821447654faf99a19d2c15e5d188'
[INFO] Commitment matches roll.
[INFO] Roll result: 2
[INFO] Game is finished.
[DEBUG] Distribution of rolls: [0, 1, 0, 0, 0, 1]
```

For ease of reading, small keys have been used for these examples. Normal runs will use more secure primes (see `constants.py`). For example, the key exchange will look like this for the client:

```log
[DEBUG] My long-term private key: 14632250342648398669102696770428647518314687168820305040332389452217684377842790754574361178359174611804711230778187813209112917029577227303536720570382271464396290088595387612211976088290332428249184263322989388154673403830558642268610189139958221369412323342274148247218518129653550927138684504057825030312668008832377752760094097201570843296571892683844325590635676908465446720834572476441792290521347600808182665527412193749995418085426599679089503584725585974036234946821518882544255849204105684496112990822325974974566141557997757355765524787488167102793261449256017991955060909481768921244184590167932753722799
[DEBUG] My long-term public key: 16925973169918962849364488641468957275785886444455674861231452040241157021336673942609672223008019011005679532588583614081757219500179352190256311858121634895198185609206278758644482990050506164249003613707910289093991258691097715766173002882534053746958084996701707394981239755425729953950478984918918545223249179102790252844501996787061747878336215699294159603879117457941022750200546810173050918566799556645143556167038119775233001897286196958848849163506156422527035574946644463656186587851724638245287538247353748485511485418078282315488499792562127680183544733881492667088640543540149169919322053902825780633923
[INFO] Other player is hosting - I will start.
[DEBUG] Diffie-Hellman key pair - Private: 18803186593714425489291985538722503253709034125393132670450982646731208300278869923567124597297377503275022513239573796789064768758236230098782205336093819834183928330564442921088111771861849171695481082665600537488994383927735634911813613928378581127519489718495625190882459552638415427661435015629178414862031413521729022167197162049911184502446951703628221921474452789712216172448608958284056723522304210711847841107576669700765791272033532545289482388377871898982116606945873391826127327217758421372651716371384873741232619868586345319527532793714921010158333281899632004344377465621679139387535401144727821533534, Public: 8167312457939173031388877981033826717719579281641523061524048111443917622311426738677692686344652262512534986785329447319412660228875940492890548069414688478229598969667251382188319091580714870846860617214270366536681608030874555276268248017067908509164551072770310071751956861296951986196631728589888265295668830961024394151167420637458306335639033044249250264419073630801829413950146684953509967342494926803129713478998423654082561141498027862069347132291129956126664975439380173381766068507890648663764079190982172289460036472785835726530640086927002127854963373368851682279427922969737373261279980584290961679773
[DEBUG] [NETWORK SEND] {"message":"{\"recipient\":\"server\",\"sender\":\"client\",\"dh_public\":\"18803186593714425489291985538722503253709034125393132670450982646731208300278869923567124597297377503275022513239573796789064768758236230098782205336093819834183928330564442921088111771861849171695481082665600537488994383927735634911813613928378581127519489718495625190882459552638415427661435015629178414862031413521729022167197162049911184502446951703628221921474452789712216172448608958284056723522304210711847841107576669700765791272033532545289482388377871898982116606945873391826127327217758421372651716371384873741232619868586345319527532793714921010158333281899632004344377465621679139387535401144727821533534\"}","signature":{"r":"13797458365949924958090694561614011774340818806968650569760589476122529817445236317546429375002153816506388466095514588532698095212591175765284240586907002300384690684664466875349704250480755886807424575227162930751783094268188131837321346075604221490197701233794147642253081201959242003613422479393087859108134741622586296060499474325897160278085581081232822906419941489723336917508750038178715407900764327881929492590580247399815462479164826065550111737810044167140145732823424708306776904612095716853944909014407738684160128810551598731672096978956300184950841942911915369922534950827618186519264567094654099015558","s":"15909828118040728616512679620002892087494796679577466155894827752126672906533524178713755497042336861180648017937647836111405447801597070696876763844862069798533394882137665838167143485631370302249560523229974683355344246273297020077538857907978204679702648664452849999744933431337308044857305407549597191593475798450869611892880843444475942909035372211638854690200497270338923831180713060274684980895089480827946377768063295335900697490111415903323165496989718388361344172684221528951841479967067009863236708551130370392638824572654943048705546676982267307317449933165009892789366312088292445259540090142956174069680"}}
[DEBUG] [NETWORK RECV] {"message":"{\"recipient\":\"client\",\"sender\":\"server\",\"dh_public\":\"15108823006687144495321866236749808044322953745013734280796594696625082050657323152786727228856212924396724461558855754825964107469318007277283266589634587868006738117039877012477640697030840820902720085441696789372971213904445933612871270397713051907140861239129255697475414029932302143146962097807153203146539516123768354771670599680811165266158990972152750308646501198848965269144811178765574412198683114002141611288627161154684471292934619398045212699707980302443459001784316874740813049193335961596558628894592102175542946782604939248542154043818617989844720556800802844403789322496043125706178272311479506529962\"}","signature":{"r":"8740553903481126076051640250077034915473820247250325150123504536279864633740679959255246055567713548073056840620500781798704494037533182747345604065343965579733983058403992549605591957518415033839388408637604208051142834711226959984793934665715370123617486029559217271617056154517188441460196444397814247554898071786212350555596544054199659984008298548489391665447865244616624488929564170313990914072800382239788861068110692486394422887235174984153740768174673273536073996540530761760183848520809958388624254915224646957253287865434110407257161997674676418470969174239612675427494239514572934110429520186772616541725","s":"11282551989409634783923572197236616736014744451127098478566299265631612138548151862328371369456891449811189950267829633529226226636684163545427684746063962311338777554483869019205889758791676890711947526471830852984125366816027074204492700279621773601761278984070383430881051599881934979312043872573019669838810902125572685074703908511676218128121733323147706819637779134439599181952670224921170039447829356524637149544192084415123076617527162035669273351484053234808636055991687125574685033789128421568069941248387099390610216307528331650245256453549055755856883696211858330025747090713947702178928196511259268908665"}}
[DEBUG] Authenticated key exchange completed with server. Shared key: 19432118956887247299322542425706985298801475743752846679554698347146917691938845247742771685525067730200281336557247586972503809846010996773761920435434367217647595855814476025795219307626003091082805917126308086386412356770115578015937441943273047548239887463596600785888179217269060105829609320779429759712019714282816887026598359332916284546871144965093971680500262206365503967777807040233066440906798398412133626379991605402692470049606563362566877497586140931946919801206458347206341313532729627487572004060458321783867448133214456048143810946909186913818138851986248903896605069642973053491769316758083454144644
...
```

## Assignment text

Alice and Bob are playing an online dice game where they must roll virtual dice representing the 6 sides of a physical dice. However, they do not trust each other and suspect that, if they can just roll dice locally on their computers, they will choose the outcome of the dice dishonestly, choosing the outcomes they need in order to win the game. In order to solve this, they want to execute a protocol among themselves to roll a dice while ensuring that they obtain an honest dice rolling outcome. Unfortunately, Alice and Bob are also using an insecure network, where they have no authenticity, confidentiality and integrity guarantees.

How can Alice and Bob play an online dice game over their insecure network when they do not trust each other?

Luckily Alice and Bob are security savvy and just had lectures on advanced cryptography and secure channels. Moreover, they have access to a Public Key Infrastructure, meaning that they know each other's public keys for a digital signature scheme.

Your assignment is to do the following steps help Alice and Bob:

1. Design a protocol that allows Alice an Bob to throw a virtual 6 sided dice over the insecure network even though they do not trust each other.

2. Explain why your protocol is secure using concepts from the lectures.

3. Implement your virtual dice protocol in a programming language of your choosing. The implementation must consist of a program representing Alice and another program representing Bob that communicate over a network (two processes running on localhost is ok). You can use any libraries or programming languages of your choosing.

You must hand in a report explaining your protocol and why it is secure as well as the code implementing your protocol.

You can choose the digital signature scheme used by Alice and Bob, meaning you can choose how their public and secret keys for the digital signature scheme looks like.

HINT: Rolling dice is just sampling a random number from 1 to 6.

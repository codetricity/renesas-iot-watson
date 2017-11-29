
DATA=$(<watson.dat)

curl -X POST -u 9a04819f-e8b1-4a0c-b836-edf1ee57e864:vjpGKMKcQbpV \
--header "Content-Type: application/json" \
--header "Accept: audio/wav" \
--data "{\"text\":$DATA}" \
--output iot-data.wav \
"https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"

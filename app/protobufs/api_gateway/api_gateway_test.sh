
username="admin"
password="admin"

keyword="true"
retries=10
interval=1
url="http://127.0.0.1:5000"

while getopts r:i:k:u: option
do
    case "${option}"
    in
        r) retries=$OPTARG;;
        i) interval=$OPTARG;;
        k) keyword=$OPTARG;;
        u) url=$OPTARG;;
    esac
done

echo "START CONTENT TEST"
echo "retries: "$retries
echo "interval: "$interval
echo "url: "$url

# Admin adicionar livro
for i in $(seq 0 $retries); do

    res_comandocriarlivro=$(curl -k -X POST -u admin:admin --header  'Content-Type: application/json' -d '{"category": [ { "name": "Test"  } ], "description": "string", "name": "Test", "photoUrl": "test", "rating": 4.55,"type": "BOOK"  }' 'https://localhost:5000/item')

    res=$res_comandocriarlivro || res=""

    if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
    fi
    exit 1
done

# Utilizador normal tenta adicionar um livro e nao consegue
for i in $(seq 0 $retries); do

    res_comandocriarlivro=$(curl -k -X POST -u saldanha:saldanha --header  'Content-Type: application/json' -d '{"category": [ { "name": "Test"  } ], "description": "string", "name": "Test", "photoUrl": "test", "rating": 4.55,"type": "BOOK"  }' 'https://localhost:5000/item')

    res=$res_comandocriarlivro || res=""

    if echo "$res" | grep -q "false"
    then
        break
    else
        sleep "$interval"
    fi
    exit 1
done
#
#
#echo "Error! Expected content not found."
#echo "Was looking for '$keyword'; not found in:"
#echo "$html"
#echo "END CONTENT TEST: Fail!"
#
#docker-compose logs --no-color --tail=1000 web > test/logs/content-test-web.txt
#docker-compose logs --no-color --tail=1000 database > test/logs/content-test-database.txt

# If desired, cat the logs or copy to GCS

exit 0
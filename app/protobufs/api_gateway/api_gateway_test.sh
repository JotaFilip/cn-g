#!/bin/bash -eu
username="admin"
password="admin"

keyword="true"
retries=5
interval=1
url="http://127.0.0.1:8443"

while getopts r:i:k:u: option
do
    case "${option}"
    in
        r) retries=$OPTARG;;
        i) interval=$OPTARG;;
        u) url=$OPTARG;;
        *) ;;

    esac
done

echo "START CONTENT TEST"
echo "retries: "$retries
echo "interval: "$interval
echo "url: "$url

token_info_admin=$(curl --request POST \
  --url 'https://saldanha.eu.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=password \
  --data username=miguelsaldanhafernandes@protonmail.com \
  --data 'password=!sedeusquiser1999' \
  --data audience=https://recommendations.sytes.net/api \
  --data 'scope=openid name email nickname read:suggest write:item delete:item write:seen write:like write:username delete:username' \
  --data 'client_id=72wQelC6FubulYS6qlY7ZhSVkyNgoTYF'\
  --data client_secret=UHqFceMIWf0pzpA3CRWggxpGDxByyn_vQuw_90OdhaoascI-t5RBha4z5sRPbNJK | jq -r '.access_token'
)
token_info_user=$(curl --request POST \
  --url 'https://saldanha.eu.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=password \
  --data username=miguelsaldanhafernandes@pm.me \
  --data 'password=leitaomaster00.' \
  --data audience=https://recommendations.sytes.net/api \
  --data 'scope=openid name email nickname read:suggest write:item delete:item write:seen write:like write:username delete:username' \
  --data 'client_id=72wQelC6FubulYS6qlY7ZhSVkyNgoTYF'\
  --data client_secret=UHqFceMIWf0pzpA3CRWggxpGDxByyn_vQuw_90OdhaoascI-t5RBha4z5sRPbNJK | jq -r '.access_token'
)




#A fazer:
#res_delete=$(curl -k -X --header "authorization: Bearer $token_info_admin" DELETE --header 'Accept: text/html' "$url/item/BOOK/12345")


#Pronto:










res_login=$(curl -k  --header "authorization: Bearer $token_info_admin" -X GET --header 'Accept: text/html' "$url/user/login")

echo "Login"
for i in $(seq 0 $retries); do
  res=$res_login || res=""

  if echo "$res" | grep -q "login"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done
res_logout=$(curl -k  --header "authorization: Bearer $token_info_admin" -X GET --header 'Accept: text/html' "$url/user/logout")

echo "Logout"
for i in $(seq 0 $retries); do
  res=$res_logout || res=""

  if echo "$res" | grep -q "logout"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

res_change_username=$(curl --header "authorization: Bearer $token_info_user" -k -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{"username": "unico"}' "$url/user")
echo "Change username"
for i in $(seq 0 $retries); do
  res=$res_change_username || res=""

  if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

res_delete_username=$(curl --header "authorization: Bearer $token_info_user" -k -X DELETE --header 'Accept: text/html' "$url/user")
echo "delete username"
for i in $(seq 0 $retries); do
  res=$res_delete_username || res=""

  if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

echo "Adicionar visto a livro que existe"
res_seen_existe=$(curl -k  --header "authorization: Bearer $token_info_admin" -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/BOOK/606e25ad5e927a606f534263/seen")
for i in $(seq 0 $retries); do
  res=$res_seen_existe|| res=""

  if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

echo "Falhar a adicionar visto a livro que nao existe"
res_seen_nao_existe=$(curl -k  --header "authorization: Bearer $token_info_admin" -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/BOOK/12345/seen")
for i in $(seq 0 $retries); do
  res=$res_seen_nao_existe || res=""

  if echo "$res" | grep -q "false"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

echo "Adicionar like a livro que existe"
res_like_existe=$(curl -k  --header "authorization: Bearer $token_info_admin" -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url"'/item/BOOK/606e25ad5e927a606f534263/like')
for i in $(seq 0 $retries); do
  res=$res_like_existe|| res=""

  if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

echo "Falhar a adicionar like a livro que nao existe"
res_like_nao_existe=$(curl -k  --header "authorization: Bearer $token_info_admin" -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url"'/item/BOOK/12345/like')
for i in $(seq 0 $retries); do
  res=$res_like_nao_existe || res=""

  if echo "$res" | grep -q "false"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done



echo "Obter um livro que existe"
res_get=$(curl -k  --header "authorization: Bearer $token_info_admin" -X  GET --header 'Accept: text/html' "$url"'/item/BOOK/606e25ad5e927a606f534263')
for i in $(seq 0 $retries); do
  res=$res_get || res=""

  if echo "$res" | grep -q "606e25ad5e927a606f534263"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

echo "Obter recomendacoes"
res_sugest=$(curl -k  --header "authorization: Bearer $token_info_admin" -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{ "tipos": [ "BOOK"] }' "$url/suggest")
for i in $(seq 0 $retries); do
  res=$res_sugest || res=""

  if echo "$res" | grep -q "{}"
    then
        sleep "$interval"
    else
        break
  fi
  echo "$res"
  exit 1
done

echo "Escolher pag"
res_page=$(curl -k  --header "authorization: Bearer $token_info_admin" -X GET --header 'Accept: text/html' "$url/lib/1")
for i in $(seq 0 $retries); do
  res=$res_page || res=""

  if echo "$res" | grep -q "BOOK"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

echo "Admin adicionar livro"
for i in $(seq 0 $retries); do

    res_comandocriarlivro=$(curl -k -X POST --header "authorization: Bearer $token_info_admin" --header  'Content-Type: application/json' -d '{"category": [ { "name": "Test"  } ], "description": "string", "name": "Test", "photoUrl": "test", "rating": 4.55,"type": "BOOK"  }' "$url/item")

    res=$res_comandocriarlivro || res=""

    if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
    fi
    echo "$res"
    exit 1
done

echo "Utilizador normal tenta adicionaar um livro e nao consegue"
for i in $(seq 0 $retries); do

    res_comandocriarlivro=$(curl -k -X POST --header "authorization: Bearer $token_info_user" --header  'Content-Type: application/json' -d '{"category": [ { "name": "Test"  } ], "description": "string", "name": "Test", "photoUrl": "test", "rating": 4.55,"type": "BOOK"  }' "$url/item")

    res=$res_comandocriarlivro || res=""

    if echo "$res" | grep -q "Unauthorized"
    then
        break
    else
        sleep "$interval"
    fi
    echo "$res"
    exit 1
done
#
#
#echo "Error! Expected content not found."
#echo "Was looking for '$keyword'; not found in:"
#echo "$html"
#
#docker-compose logs --no-color --tail=1000 web > test/logs/content-test-web.txt
#docker-compose logs --no-color --tail=1000 database > test/logs/content-test-database.txt

# If desired, cat the logs or copy to GCS

exit 0

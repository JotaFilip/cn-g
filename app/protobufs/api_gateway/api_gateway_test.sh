#!/bin/bash -eu
username="admin"
password="admin"

keyword="true"
retries=5
interval=1
url="http://127.0.0.1:5000"

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

token_info_admin = $(curl --request POST \
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
token_info_user = $(curl --request POST \
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
res_get=$(curl -k  --header "authorization: Bearer $token_info_admin" -X  GET --header 'Accept: text/html' "$url"'/item/BOOK/607615b3aeb60e0f26f7c1df')

res_like_existe=$(curl -k  --header "authorization: Bearer $token_info_admin" -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url"'/item/BOOK/607615b3aeb60e0f26f7c1df/like')
res_like_nao_existe=$(curl -k  --header "authorization: Bearer $token_info_admin" -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url"'/item/BOOK/12345/like')

res_seen_existe=$(curl -k  --header "authorization: Bearer $token_info_admin" -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/BOOK/607615b3aeb60e0f26f7c1df/seen")
res_seen_nao_existe=$(curl -k  --header "authorization: Bearer $token_info_admin" -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/BOOK/12345/seen")

res_page=$(curl -k  --header "authorization: Bearer $token_info_admin" -X GET --header 'Accept: text/html' "$url/lib/1")

res_sugest=$(curl -k  --header "authorization: Bearer $token_info_admin" -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{ "tipos": [ "BOOK"] }' "$url/suggest")
#TODO
res_change_password=$(curl --header "authorization: Bearer $token_info_user" -k -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{ "password": "saldanha", "username": "saldanha"}' "$url/user/search/saldanha")
res_login=$(curl -k  --header "authorization: Bearer $token_info_admin" -X GET --header 'Accept: text/html' "$url/user/login")
res_logout=$(curl -k  --header "authorization: Bearer $token_info_admin" -X GET --header 'Accept: text/html' "$url/user/logout")

echo "Login"
for i in $(seq 0 $retries); do
  res=$res_login || res=""

  if echo "$res" | grep -q "html"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

echo "Logout"
for i in $(seq 0 $retries); do
  res=$res_logout || res=""

  if echo "$res" | grep -q "OK"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

echo "Adicionar visto a livro que existe"
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
for i in $(seq 0 $retries); do
  res=$res_get || res=""

  if echo "$res" | grep -q "607615b3aeb60e0f26f7c1df"
    then
        break
    else
        sleep "$interval"
  fi
  echo "$res"
  exit 1
done

echo "Obter recomendacoes"
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

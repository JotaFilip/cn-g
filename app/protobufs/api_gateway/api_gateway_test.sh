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

#A fazer:
#res_delete=$(curl -k -X -u admin:admin DELETE --header 'Accept: text/html' "$url/item/BOOK/12345")


#Pronto:
res_get=$(curl -k  -u admin:admin -X  GET --header 'Accept: text/html' "$url"'/item/BOOK/607615b3aeb60e0f26f7c1df')

res_like_existe=$(curl -k  -u admin:admin -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url"'/item/BOOK//607615b3aeb60e0f26f7c1dflike')
res_like_nao_existe=$(curl -k  -u admin:admin -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url"'/item/BOOK/12345/like')

res_seen_existe=$(curl -k  -u admin:admin -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/BOOK/607615b3aeb60e0f26f7c1df/seen")
res_seen_nao_existe=$(curl -k  -u admin:admin -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/BOOK/12345/seen")

res_page=$(curl -k  -u admin:admin -X GET --header 'Accept: text/html' "$url/lib/1")

res_sugest=$(curl -k  -u admin:admin -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{ "tipos": [ "BOOK"] }' "$url/suggest")
#TODO
res_change_password=$(curl -u saldanha:saldanha -k -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{ "password": "saldanha", "username": "saldanha"}' "$url/user/search/saldanha")
res_login=$(curl -k  -u admin:admin -X GET --header 'Accept: text/html' "$url/user/login")
res_logout=$(curl -k  -u admin:admin -X GET --header 'Accept: text/html' "$url/user/logout")

echo "Login"
for i in $(seq 0 $retries); do
  res=$res_login || res=""

  if echo "$res" | grep -q "token"
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

  if echo "$res" | grep -q "Logged Out"
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

    res_comandocriarlivro=$(curl -k -X POST -u admin:admin --header  'Content-Type: application/json' -d '{"category": [ { "name": "Test"  } ], "description": "string", "name": "Test", "photoUrl": "test", "rating": 4.55,"type": "BOOK"  }' "$url/item")

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

    res_comandocriarlivro=$(curl -k -X POST -u saldanha:saldanha --header  'Content-Type: application/json' -d '{"category": [ { "name": "Test"  } ], "description": "string", "name": "Test", "photoUrl": "test", "rating": 4.55,"type": "BOOK"  }' "$url/item")

    res=$res_comandocriarlivro || res=""

    if echo "$res" | grep -q "false"
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
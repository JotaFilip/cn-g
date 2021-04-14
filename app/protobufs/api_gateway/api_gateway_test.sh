
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
        u) url=$OPTARG;;
        *) ;;

    esac
done

echo "START CONTENT TEST"
echo "retries: "$retries
echo "interval: "$interval
echo "url: "$url

#A fazer:
#res_delete=$(curl -k -X -u admin:admin DELETE --header 'Accept: text/html' "$url/item/12345/BOOK")


#Pronto:
res_get=$(curl -k -X -u admin:admin GET --header 'Accept: text/html' "$url/item/607615b3aeb60e0f26f7c1df/BOOK")

res_like_existe=$(curl -k -X -u admin:admin PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/607615b3aeb60e0f26f7c1df/BOOK/like")
res_like_nao_existe=$(curl -k -X -u admin:admin PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/12345/BOOK/like")

res_seen_existe=$(curl -k -X -u admin:admin PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/607615b3aeb60e0f26f7c1df/BOOK/seen")
res_seen_nao_existe=$(curl -k -X -u admin:admin PUT --header 'Content-Type: application/json' --header 'Accept: text/html' "$url/item/12345/BOOK/seen")

res_page=$(curl -k -X -u admin:admin GET --header 'Accept: text/html' "$url/lib/1")

res_sugest=$(curl -k -X -u admin:admin POST --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{ "tipos": [ "BOOK"] }' "$url/suggest")
#TODO
res_change_password=$(curl -u saldanha:saldanha -k -X PUT --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{ "password": "saldanha", "username": "saldanha"}' "$url/user/search/saldanha")
res_login=$(curl -k -X -u admin:admin GET --header 'Accept: text/html' "$url/user/login")
res_logout=$(curl -k -X -u admin:admin GET --header 'Accept: text/html' "$url/user/logout")

# Login
for i in $(seq 0 $retries); do
  res=$res_login || res=""

  if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
  fi
  exit 1
done

# Logout
for i in $(seq 0 $retries); do
  res=$res_logout || res=""

  if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
  fi
  exit 1
done

# Adicionar visto a livro que existe
for i in $(seq 0 $retries); do
  res=$res_seen_existe|| res=""

  if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
  fi
  exit 1
done

# Falhar a adicionar visto a livro que nao existe
for i in $(seq 0 $retries); do
  res=$res_seen_nao_existe || res=""

  if echo "$res" | grep -q "false"
    then
        break
    else
        sleep "$interval"
  fi
  exit 1
done

# Adicionar like a livro que existe
for i in $(seq 0 $retries); do
  res=$res_like_existe|| res=""

  if echo "$res" | grep -q "true"
    then
        break
    else
        sleep "$interval"
  fi
  exit 1
done

# Falhar a adicionar like a livro que nao existe
for i in $(seq 0 $retries); do
  res=$res_like_nao_existe || res=""

  if echo "$res" | grep -q "false"
    then
        break
    else
        sleep "$interval"
  fi
  exit 1
done

# Obter um livro que existe
for i in $(seq 0 $retries); do
  res=$res_get || res=""

  if echo "$res" | grep -q "607615b3aeb60e0f26f7c1df"
    then
        break
    else
        sleep "$interval"
  fi
  exit 1
done

# Obter recomendacoes
for i in $(seq 0 $retries); do
  res=$res_sugest || res=""

  if echo "$res" | grep -q "{}"
    then
        sleep "$interval"
    else
        break
  fi
  exit 1
done

# Escolher pag
for i in $(seq 0 $retries); do
  res=$res_page || res=""

  if echo "$res" | grep -q "BOOK"
    then
        break
    else
        sleep "$interval"
  fi
  exit 1
done

# Admin adicionar livro
for i in $(seq 0 $retries); do

    res_comandocriarlivro=$(curl -k -X POST -u admin:admin --header  'Content-Type: application/json' -d '{"category": [ { "name": "Test"  } ], "description": "string", "name": "Test", "photoUrl": "test", "rating": 4.55,"type": "BOOK"  }' "$url/item")

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

    res_comandocriarlivro=$(curl -k -X POST -u saldanha:saldanha --header  'Content-Type: application/json' -d '{"category": [ { "name": "Test"  } ], "description": "string", "name": "Test", "photoUrl": "test", "rating": 4.55,"type": "BOOK"  }' "$url/item")

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
#
#docker-compose logs --no-color --tail=1000 web > test/logs/content-test-web.txt
#docker-compose logs --no-color --tail=1000 database > test/logs/content-test-database.txt

# If desired, cat the logs or copy to GCS

exit 0
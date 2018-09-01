# 개요

## RabbitMQ 샘플 소스 모음
스터디 중 작성한 코드를 간단하게 정리한다. 모든 코드는 아래 라이브러리를 사용한다.
- pika
- rabbitpy

# 메시지 발행

## RabbitMQ 기본 연동
- 자세한 설명은 생략한다.
- consume_pika.py
- consume_rabbipy.py
- publish_pika.py
- publish_rabbitpy.py

## mandatory 플래그 설정

- publish_mandatory_rabbitpy.py

익스체인지가 메시지를 라우팅할 수 없다면, 메시지를 되돌려 보내도록 하기 위해서는 mandatory=True 를 설정하면 된다.
````python
message.publish(exchange, 
                'example-routing-key-not',
                mandatory=True)
````
실행하면 아래와 같은 메시지가 출력된다. 

rabbitpy.exceptions.MessageReturnedException: Message was returned by RabbitMQ: (312) for exchange NO_ROUTE

## 메시지 발행 정상 확인

- publish_confirm_rabbitpy.py



````python
channel.enable_publisher_confirms()
...
if message.publish(exchange, 'example-routing-key'):
    print('message OK')
````

비동기로 처리하지만 확인을 받는 시점을 정확히 알 수 없다. 또한 확인을 받을 때까지 블로킹되므로 느리다. 


## 트랜잭션 처리

- publish_transaction_rabbitpy.py

트랜잭션은 발행자가 RabbitMQ 메시지 브로커의 큐에 메시지를 성공적으로 전달했음을 알리는 데 사용한다. 

## RabbitMQ 아키텍처를 위해 고려할 사항

RabbitMQ in Depth 117 page 참고

- 발행자가 메시지를 디스크에 저장해야 하는가?
- 애플리케이션의 다양한 구성 요소는 ㅂ라행된 메시지가 수신됐는지 보장해야 하는가?
- TCP 배압으로 애플리케이션이 차단되거나 RabbitMQ에 메시지를 발행하는 동안 연결이 차된된 경우는 어떻게 되는가?
- 메시지가 얼마나 중요한가? 메시지 처리량을 높이기 위해 배달 보장을 희생할 수 있는가?

# 메시지 수신




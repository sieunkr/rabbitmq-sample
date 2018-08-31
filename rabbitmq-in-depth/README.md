

## RabbitMQ 샘플 소스 모음
스터디 중 작성한 코드를 간단하게 정리한다. 모든 코드는 아래 라이브러리를 사용한다.
- pika
- rabbitpy

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

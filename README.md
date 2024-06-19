# django-youtube-restapi

### (1) Project Settings

- GitHub

## Model 구조 => ORM

(1) User => users
- email
- password
- nickname
- is_business

(2) Video => videos
- title
- description
- link
- views_count
- thumbnail
- video_file: link or file
- User: FK

ex) 파일(이미지, 동영상) 
=> 장고에 부하가 걸림
=> S3 Bucket(저렴, 속도가 빠름) -> 결과물: 링크 

(3) Reaction => reactions
- User: FK
- Video: FK
- reaction (like, dislike, cancel) => 실제 youtube rest api

(4) Comment => comments
- User: FK
- Video: FK
- content
- like
- dislike

(5) Subscription => subscriptions
- User: FK => Subscriber (내가 구독한 사람)
- User: FK => Subscribed_to (나를 구독한 사람)

(6) Common => common
- created_at
- updated_at


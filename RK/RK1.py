# Написать класс Twitter, в котором есть следующие методы:
# * __init__(self), который инициализирует класс
# * post_tweet(self, user_id, tweet_id), который создает новый твит с идентификатором tweet_Id по 
#   идентификатору пользователя user_id. Каждый вызов этой функции будет осуществляться с уникальным
#   идентификатором твита. Желательно, чтобы впоследствии твиты можно было бы быстро получить по user_id.
# * get_news_feed(self, user_id), который получает 10 последних идентификаторов твитов в ленте новостей
#   пользователя. Каждый элемент в ленте новостей должен быть опубликован пользователями, на которых
#   подписан пользователь. Твиты должны быть упорядочены от самого позднего до самого раннего. Подумайте,
#   как организовать упорядочивание твитов по времени:
#   * возможно для этого лучше записывать в структуру данных с твитами 
#       * информацию о твите (то есть tweet_id)
#       * какое то число, отвечающее за время (например какой нибудь счетчик)
#   * и это например завернуть в кортеж
# * follow(self, follower_id, followee_id), в котором пользователь с идентификатором follower_id подписался
#   на пользователя с идентификатором followee_id. Желательно, чтобы впоследствии подписки можно было бы
#   быстро получить по follower_id.
# * unfollow(self, follower_id, followee_id), в котором пользователь с идентификатором follower_id отписался
#   от пользователя с идентификатором followee_id.

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from typing import List

class Twitter:
    def _create_counter(self):
        i = 0

        def func():
            nonlocal i
            i += 1
            return i

        return func

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.counter = self._create_counter()

    def post_tweet(self, user_id, tweet_id):
        if user_id not in self.tweets:
            self.tweets[user_id] = []
        self.tweets[user_id].append( ( tweet_id, self.counter() ) )

    def get_news_feed(self, user_id) -> List[int]:
        tweets = []
        if user_id not in self.followers:
            return tweets

        for tweet_user in self.followers[user_id]:
            if tweet_user in self.tweets:
                tweets += self.tweets[tweet_user]

        tweets.sort(key=lambda a: a[1], reverse=True)
        return [ it[0] for it in tweets[:10] ]

    def follow(self, follower_id, followee_id):
        if follower_id not in self.followers:
            self.followers[follower_id] = set()
        self.followers[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        if follower_id in self.followers:
            if followee_id in self.followers[follower_id]:
                self.followers[follower_id].remove(followee_id)

#'''
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
'''
twitter = Twitter()
twitter.follow(1, 2)
twitter.follow(1, 3)
twitter.post_tweet(2, 4)
twitter.post_tweet(2, 6)
twitter.post_tweet(3, 2)
twitter.post_tweet(3, 7)
twitter.post_tweet(3, 3)
twitter.post_tweet(3, 8)
twitter.post_tweet(2, 1)
twitter.post_tweet(2, 9)
twitter.follow(1, 4)
twitter.post_tweet(4, 5)
twitter.post_tweet(4, 10)
twitter.unfollow(1, 2)
twitter.post_tweet(5, 11)
twitter.post_tweet(5, 12)
twitter.post_tweet(5, 13)
twitter.post_tweet(6, 14)
twitter.follow(1, 5)
twitter.post_tweet(7, 15)
twitter.post_tweet(7, 16)
twitter.post_tweet(7, 17)
twitter.post_tweet(7, 18)
twitter.follow(1, 7)
print(twitter.get_news_feed(1))
'''

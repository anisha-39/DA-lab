from neo4j import GraphDatabase
import tweepy

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

class Neo4jConnector:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def insert_data(self, tweet_id, user_name, text, sentiment, keywords):
        with self.driver.session() as session:
            session.execute_write(
                self._create_tweet,
                tweet_id, user_name, text, sentiment, keywords
            )

    @staticmethod
    def _create_tweet(tx, tweet_id, user_name, text, sentiment, keywords):
        query = """
        MERGE (u:User {name: $user_name})
        MERGE (t:Tweet {id: $tweet_id, text: $text, sentiment: $sentiment})
        MERGE (u)-[:POSTED]->(t)
        WITH t
        UNWIND $keywords AS keyword
        MERGE (k:Keyword {name: keyword})
        MERGE (t)-[:MENTIONS]->(k)
        """
        tx.run(
            query,
            tweet_id=tweet_id,
            user_name=user_name,
            text=text,
            sentiment=sentiment,
            keywords=keywords,
        )

neo4j_conn = Neo4jConnector(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

def predict_sentiment(tweet):
    tweet = tweet.lower()
    if any(word in tweet for word in ["good", "great", "happy", "love", "excellent"]):
        return "Positive"
    elif any(word in tweet for word in ["bad", "sad", "hate", "worst", "poor"]):
        return "Negative"
    else:
        return "Neutral"

class MyStreamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        try:
            tweet_id = tweet.id
            text = tweet.text
            user_name = "unknown_user"

            sentiment = predict_sentiment(text)
            keywords = ["brand"]

            neo4j_conn.insert_data(tweet_id, user_name, text, sentiment, keywords)

            print("Tweet:", text)
            print("Sentiment:", sentiment)
            print()

        except Exception as e:
            print("Error:", str(e))

BEARER_TOKEN = "your_actual_bearer_token_here"

stream = MyStreamListener(BEARER_TOKEN)
stream.add_rules(tweepy.StreamRule("brand"))
stream.filter()
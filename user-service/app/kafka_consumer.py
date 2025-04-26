# # from kafka import KafkaConsumer
# # from sqlalchemy import create_engine, Column, Integer, String, JSON, Table, MetaData
# # from sqlalchemy.orm import sessionmaker
# # import json
# # import os

# # # Kafka settings
# # topics = ['user-events-topic']

# # consumer = KafkaConsumer(
# #     *topics,
# #     bootstrap_servers=os.getenv('KAFKA_BROKER', 'localhost:9092'),
# #     group_id='user-events-group',
# #     auto_offset_reset='earliest',
# #     enable_auto_commit=True,
# #     value_deserializer=lambda m: json.loads(m.decode('utf-8'))
# # )

# # # Database setup
# # DATABASE_URL = "sqlite:///users.db"  # SQLite file users.db
# # engine = create_engine(DATABASE_URL, echo=True)
# # metadata = MetaData()

# # # Define user table
# # users_table = Table(
# #     'users', metadata,
# #     Column('id', Integer, primary_key=True),
# #     Column('username', String),
# #     Column('email', String),
# #     Column('phonenumber', String),
# # )

# # # Create tables if not exist
# # metadata.create_all(engine)

# # # Create a session
# # Session = sessionmaker(bind=engine)
# # session = Session()

# # print(f"Listening to topics: {topics}")

# # try:
# #     for message in consumer:
# #         event = message.value
# #         event_type = event.get('event_type')
# #         details = event.get('details', {})
# #         user_id = event.get('user_id')

# #         print(f"\nReceived event: {event_type} for User ID: {user_id}")

# #         if event_type == "user.created":
# #             # Insert new user
# #             insert_stmt = users_table.insert().values(
# #                 id=user_id,
# #                 username=details.get('username'),
# #                 email=details.get('email'),
# #                 phone=details.get('phone')
# #             )
# #             session.execute(insert_stmt)
# #             session.commit()

# #         elif event_type == "user.updated":
# #             # Update existing user
# #             update_stmt = users_table.update().where(users_table.c.id == user_id).values(
# #                 username=details.get('username'),
# #                 email=details.get('email'),
# #                 phonenumber=details.get('phonenumber')
# #             )
# #             session.execute(update_stmt)
# #             session.commit()

# #         elif event_type == "user.deleted":
# #             # Delete user
# #             delete_stmt = users_table.delete().where(users_table.c.id == user_id)
# #             session.execute(delete_stmt)
# #             session.commit()

# #         else:
# #             print(f"Unknown event type: {event_type}")

# # except KeyboardInterrupt:
# #     print("Stopping consumer...")
# # finally:
# #     session.close()
# #     consumer.close()

# from kafka import KafkaConsumer
# import json

# consumer = KafkaConsumer(
#     'user.created',
#     'user.updated',
#     'user.deleted',
#     bootstrap_servers='localhost:9092',
#     group_id='user-events-group',
#     value_deserializer=lambda m: json.loads(m.decode('utf-8')),
#     auto_offset_reset='earliest'
# )

# print("Listening for user events...")

# try:
#     for msg in consumer:
#         print(f"\n[Received on topic {msg.topic}] {msg.value}")
# except KeyboardInterrupt:
#     print("Stopping consumer...")

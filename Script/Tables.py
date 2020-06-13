# Script to create the "Candidates" and "Vote Share" tables

from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Set table_id to the ID of the table to create.
project_id = "promising-lamp-273900"
dataset_id = 'candidates'
candidate_table_id = 'candidatesInfo'
vote_share_table_id = "vote_share"

candidate_table = project_id+"."+dataset_id+"."+candidate_table_id
vote_share_table = project_id+"."+dataset_id+"."+vote_share_table_id

schema_candidate = [
    bigquery.SchemaField("ridingNumber", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("CONCandidateName", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("LIBCandidateName", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("GRNCandidateName", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("NDPCandidateName", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("BQCandidateName", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("PPCCandidateName", "STRING", mode="NULLABLE"),
]

schema_vote_share = [
    bigquery.SchemaField("ridingNumber", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("ridingNameEnglish", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("ridingNameFrench", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("totalVotes", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("turnout", "NUMERIC", mode="NULLABLE"),
    bigquery.SchemaField("conservativeVoteShare", "NUMERIC", mode="NULLABLE"),
    bigquery.SchemaField("liberalVoteShare", "NUMERIC", mode="NULLABLE"),
    bigquery.SchemaField("NDPVoteShare", "NUMERIC", mode="NULLABLE"),
    bigquery.SchemaField("greenVoteShare", "NUMERIC", mode="NULLABLE"),
    bigquery.SchemaField("blocQuebecoisVoteShare", "NUMERIC", mode="NULLABLE"),
    bigquery.SchemaField("peoplePartyVoteShare", "NUMERIC", mode="NULLABLE")
]

candidate = bigquery.Table(candidate_table, schema=schema_candidate)
vote_share = bigquery.Table(vote_share_table, schema=schema_vote_share)

candidate_table_request = client.create_table(candidate)  # Make an API request.
vote_share_table_request = client.create_table(vote_share)  # Make an API request.

print("Created table {}.{}.{}".format(candidate_table_request.project, candidate_table_request.dataset_id, candidate_table_request.table_id))
print("Created table {}.{}.{}".format(vote_share_table_request.project, vote_share_table_request.dataset_id, vote_share_table_request.table_id))

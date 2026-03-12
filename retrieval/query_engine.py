def create_query_engine(index):

    query_engine = index.as_query_engine(
        similarity_top_k=2,
        response_mode="compact"
    )

    return query_engine
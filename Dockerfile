FROM python:3.12-slim-bookworm
# We use pipx to install uv in a separate environment
# We install specific version
RUN python3 -m pip install --user pipx==1.5.0
# We modify the path so we can just use 'uv' and 'pipx'
ENV PATH="${PATH}:/root/.local/bin"
# We install specific version
RUN pipx install uv==0.1.44
WORKDIR /model-service
# We copy only the requirements first, because they change less frequently
COPY requirements.txt .
RUN uv pip sync requirements.txt
COPY entrypoint.sh .
# Now we copy the src
COPY src .
ENTRYPOINT ["./entrypoint.sh"]
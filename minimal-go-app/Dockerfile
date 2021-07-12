FROM golang:1.16 AS build
WORKDIR /go/src/github.com/PhilomathesInc/demo-applications/minimal-go-app
COPY go.mod .
COPY go.sum .
COPY *.go .
RUN CGO_ENABLED=0 GOOS=linux go build -o /minimal-go-app

FROM gcr.io/distroless/base-debian10
WORKDIR /
COPY --from=build /minimal-go-app /minimal-go-app
EXPOSE 8080
USER nonroot:nonroot
ENTRYPOINT ["/minimal-go-app"]

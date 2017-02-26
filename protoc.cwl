class: CommandLineTool
cwlVersion: v1.0
requirements:
  DockerRequirement:
    dockerImageId: ga4gh-wes/protoc
    dockerFile:
      $include: protoc.Dockerfile
baseCommand: protoc
arguments:
  - -I
  - /usr/local/include
  - -I
  - /usr/local/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis
inputs:
  includes:
    type:
      type: array
      items: Directory
      inputBinding:
        prefix: -I
    inputBinding:
      position: 1
  swg:
    type: string
    inputBinding:
      position: 2
    default: --swagger_out=logtostderr=true:.
  proto:
    type: File
    inputBinding:
      position: 3
outputs:
  outfile:
    type: File
    outputBinding:
      glob: '*.json'
